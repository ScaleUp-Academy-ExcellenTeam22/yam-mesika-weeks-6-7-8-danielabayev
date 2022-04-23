import UserManagement
import os
import imghdr


class BinaryFile:
    """
    Class for handle binary files.
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

    def get_dimensions(self) -> list:
        """
        This function returns the dimensions of the file if it's a picture or None if it's not a picture.
        :return: The dimensions of the image or None.
        """
        if imghdr.what(self.path):
            pass
        else:
            return None
