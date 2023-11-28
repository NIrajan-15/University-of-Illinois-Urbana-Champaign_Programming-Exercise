# Description: This file contains the Completion class, which represents a completed training.

class Completion:
    def __init__(self, training_name, completion_timestamp, expiration_date):
        """
        Initializes a Completion object with training information.

        Parameters:
        - training_name (str): The name of the completed training.
        - completion_timestamp (str): The timestamp when the training was completed.
        - expiration_date (str): The expiration date of the training (can be None if no expiration).

        Attributes:
        - training_name (str): The name of the completed training.
        - completion_timestamp (str): The timestamp when the training was completed.
        - expiration_date (str): The expiration date of the training (can be None if no expiration).
        """
        self.training_name = training_name
        self.completion_timestamp = completion_timestamp
        self.expiration_date = expiration_date

    def to_dict(self):
        """
        Converts the Completion object to a dictionary.

        Returns:
        dict: A dictionary representing the Completion object.
        """
        return {
            "training_name": self.training_name,
            "completion_timestamp": self.completion_timestamp,
            "expiration_date": self.expiration_date
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Completion object from a dictionary.

        Parameters:
        - data (dict): A dictionary containing Completion data.

        Returns:
        Completion: A Completion object created from the provided dictionary.
        """
        return Completion(data["name"], data['timestamp'], data['expires'])
