#Description: Person class for the training completion tracker.

# import completion class from completion.py
from completion import Completion

class Person:
    def __init__(self, name, completions):
        """
        Initializes a Person object with name and completions.

        Parameters:
        - name (str): The name of the person.
        - completions (list): List of Completion objects associated with the person.

        Attributes:
        - name (str): The name of the person.
        - completions (list): List of the latest Completion objects associated with the person.
        """
        self.name = name
        self.completions = self.get_latest_completions(completions)

    def to_dict(self):
        """
        Converts the Person object to a dictionary.

        Returns:
        dict: A dictionary representing the Person object.
        """
        return {
            "name": self.name,
            "completions": [completion.to_dict() for completion in self.completions]
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Person object from a dictionary.

        Parameters:
        - data (dict): A dictionary containing Person data.

        Returns:
        Person: A Person object created from the provided dictionary.
        """
        return Person(data['name'], [Completion.from_dict(completion_data) for completion_data in data['completions']])

    def get_latest_completions(self, completions):
        """
        Returns the list of latest completions for each training.

        Parameters:
        - completions (list): List of Completion objects.

        Returns:
        list: List of the latest Completion objects for each training.
        """
        # Create a dictionary to store the latest completion for each training
        latest_completion_dict = {}
        for completion in completions:
            # If there is no latest completion or the current completion is more recent, update the dictionary
            if completion.training_name not in latest_completion_dict or completion.completion_timestamp > latest_completion_dict[completion.training_name].completion_timestamp:
                latest_completion_dict[completion.training_name] = completion

        # Return the values (latest completions) from the dictionary
        return list(latest_completion_dict.values())
