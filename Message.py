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

    def __str__(self):
        return "{sender} send the message: {message}".format(sender=self.sender,message=self.body)

    def __repr__(self):
        return self.__str__()