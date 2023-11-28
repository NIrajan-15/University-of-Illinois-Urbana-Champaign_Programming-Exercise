# Author: Nirajan Sangraula
# Date: 11/26/2023
# Description: This program reads training data from a JSON file and performs the specified tasks and writes the results to JSON files.
'''
1. List each completed training with a count of how many people have completed that training.
2. Given a list of trainings and a fiscal year (defined as 7/1/n-1 – 6/30/n), for each specified training, list all people that completed that training in the specified fiscal year.
   Use parameters: Trainings = "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"; Fiscal Year = 2024
3. Given a date, find all people that have any completed trainings that have already expired, or will expire within one month of the specified date (A training is considered expired the day after its expiration date). For each person found, list each completed training that met the previous criteria, with an additional field to indicate expired vs expires soon.
   Use date: Oct 1st, 2023
'''

import json
# import datetime and timedelta from datetime module
from datetime import datetime, timedelta
# import Person class from person.py
from person import Person

class TrainingManager:

    @staticmethod
    def is_in_fiscal_year(timestamp, fiscal_year):
        """
        Checks if the completion timestamp is within the specified fiscal year.

        Parameters:
        - timestamp (str): The completion timestamp in the format '%m/%d/%Y'.
        - fiscal_year (int): The fiscal year.

        Returns:
        bool: True if within fiscal year, False otherwise.
        """
        # Convert the timestamp to a datetime object
        completion_date = datetime.strptime(timestamp, "%m/%d/%Y")
        start_date = datetime(fiscal_year - 1, 7, 1)
        end_date = datetime(fiscal_year, 6, 30)
        return start_date <= completion_date <= end_date
    

    @staticmethod
    def write_to_json_file(data, output_file):
        """
        Writes data to a JSON file.

        Parameters:
        - data (list/dict): Data to be written to the file.
        - output_file (str): Name of the output JSON file.
        """
        try:
            with open(output_file, 'w') as file:
                # write data to the file
                json.dump(data, file, indent=2)
        except Exception as e:
            # Handle the exception, e.g., print an error message or log the issue
            print(f"Error writing to JSON file: {e}")


    def __init__(self, training_file):
        """
        Constructor for TrainingManager.

        Parameters:
        - training_file (str): Name of the JSON file containing training data.
        """
        self.people = self.load_from_json(training_file)


    def load_from_json(self, training_file):
        """
        Loads data from a JSON file and creates Person objects.

        Parameters:
        - training_file (str): Name of the JSON file containing training data.

        Returns:
        list: List of Person objects.
        """
        try:
            with open(training_file, 'r') as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            # Handle the exception, e.g., print an error message or log the issue
            print(f"Error loading JSON data: {e}")
            # Optionally, you can raise the exception again or return a default value
            return []

        return [Person.from_dict(person_data) for person_data in data]

    def get_training_complete_count(self):
        """
        Returns the count of each training completed by people.

        Returns:
        list: List of dictionaries with training names and completion counts.
        """
        training_count = {}

        for person in self.people:
            for completion in person.completions:
                # If the training is not in the dictionary, add it with a count of 1
                training_count[completion.training_name] = training_count.get(completion.training_name, 0) + 1

        return [{"training": training, "count": count} for training, count in training_count.items()]
    
    
    def get_completed_training_by_fiscal_year(self, trainings, fiscal_year):
        """
        Returns a list of dictionaries with specified trainings and all people who completed each training.

        Parameters:
        - trainings (list): List of training names.
        - fiscal_year (int): The fiscal year.

        Returns:
        list: List of dictionaries with training names and lists of people who completed each training.
        """
        result = {training: [] for training in trainings}

        for person in self.people:
            for completion in person.completions:
                if completion.training_name in trainings and self.is_in_fiscal_year(completion.completion_timestamp, fiscal_year):
                    result[completion.training_name].append({"name": person.name})

        return [{"training": training, "completed_by": data} for training, data in result.items() if data]


    def get_expired_training(self, specified_expiry_date):
        """
        Returns people with expiring trainings before the specified expiry date.

        Parameters:
        - specified_expiry_date (str): The specified expiry date.

        Returns:
        list: List of dictionaries with person names and expiring trainings.
        """
        specified_expiry_date = datetime.strptime(specified_expiry_date, "%b %dst, %Y")
        result = []
        
        for person in self.people:
            expiring_trainings = []
            for completion in person.completions:
                if completion.expiration_date:
                    # Convert the expiration date to a datetime object in format '%m/%d/%Y'
                    training_expiration_date = datetime.strptime(completion.expiration_date, "%m/%d/%Y")
                    status = ""
                    if training_expiration_date < specified_expiry_date:
                        status = "Expired"
                    elif specified_expiry_date <= training_expiration_date <= specified_expiry_date + timedelta(days=30):
                        status = "Expires soon"
                    
                    # If the training is expiring or soon to expire, add it to the list
                    if status!="":
                        expiring_trainings.append({"training": completion.training_name, "status": status})
            # If the person has any expiring trainings, add them to the list
            if expiring_trainings:
                result.append({"name": person.name, "ExpiringTrainings": expiring_trainings})

        return result


