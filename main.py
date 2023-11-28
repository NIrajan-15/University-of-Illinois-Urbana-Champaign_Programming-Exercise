import os
from trainingManager import TrainingManager

# main function for running the program
def main():
    # Create a TrainingManager object with the training file
    training_manager = TrainingManager("trainings.txt")

    # Change the fiscal year, expiry date, and fiscal_year_training_list as needed
    fiscal_year = 2024
    expiry_date = "Oct 1st, 2023"
    fiscal_year_training_list = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]

    # Create an 'output' folder if it doesn't exist
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Call functions from the TrainingManager object as needed and write the results as JSON files to output folder

    # get the count of people who have completed each training
    training_count_data = training_manager.get_training_complete_count()
    training_manager.write_to_json_file(training_count_data, os.path.join(output_folder, "Each training count.json"))

    # get the list of people who have completed each training in the specified fiscal year
    fiscal_year_completion_data = training_manager.get_completed_training_by_fiscal_year(fiscal_year_training_list, fiscal_year)
    training_manager.write_to_json_file(fiscal_year_completion_data, os.path.join(output_folder, "Fiscal year "+ str(fiscal_year) +" training completion.json"))

    # get the list of people who have completed any training that has expired or will expire within one month of the specified date
    expired_training_data = training_manager.get_expired_training(expiry_date)
    training_manager.write_to_json_file(expired_training_data, os.path.join(output_folder, "Expired or expiring soon trainings.json"))

if __name__ == "__main__":
    main()
