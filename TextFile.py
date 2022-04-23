import UserManagement
import os


class TextFile:
    """
    Class for handle text files.
    """
    def __init__(self, path: str, creator: UserManagement):
        """
        Constructor.
        :param path: The path to the file.
        :param creator: The creator of the file.
        """
        self.size = os.path.getsize(path)
        self.user_creator = creator
        self.path = path

    def count(self, string: str) -> float:
        """
        This function receives a string and returns the number of times the string appears in the file.
        :param string: The string to check.
        :return: The number of times the string appears in the file.
        """
        data = self.read(self, self.user_creator)
        return data.count(string)

    def read(self, user: UserManagement) -> str:
        """
        The function receives a user and returns the file content if the user is the creator and none otherwise.
        :param user: The user name.
        :return: The file content if the user creates the file or None otherwise.
        """
        if user == self.user_creator:
            file = open(self.path)
            return file.read()
        else:
            return None
