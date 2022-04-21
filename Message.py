class Message:
    """
    A messages class.
    Users send messages using this class.
    """

    def __init__(self, message_id, body, sender):
        self.read = False
        self.sender = sender
        self.body = body
        self.id = message_id

    def __str__(self) -> str:
        """
        This function returns a user-friendly description of the object.
        :return: The string of the object.
        """
        return "{sender} send the message: {message}".format(sender=self.sender,message=self.body)

    def __repr__(self) -> str:
        """
        This function returns a developer-friendly string representation of an object.
        :return: The string of the object.
        """
        return self.__str__()

    def __len__(self) -> int:
        """
        This function returns a positive integer that represents the length of the message.
        :return: The message length.
        """
        return len(self.body)
