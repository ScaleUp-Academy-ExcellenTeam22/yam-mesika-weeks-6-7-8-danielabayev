import Message


class PostOffice:
    """A Post Office class. Allows users to message each other.
    Args:
        usernames (list): Users for which we should create PO Boxes.
    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.
        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.
        Returns:
            int: The message ID, auto incremented number.
        Raises:
            KeyError: If the recipient does not exist.
        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.
            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message.Message(id, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name: str, number_of_messages: int = None) -> list:
        """
        This function receive user name and number of messages to read and return list of the messages.
        In order to do the function I add read key in the message dictionary this key receive boolean value.
        :param user_name: The user name.
        :param number_of_messages: The numbers of the wanted messages to read.
        :return: List of the messages.
        """
        user_box = self.boxes[user_name]
        return_box = []
        mail_number_in_user_box, mail_to_add_number = 0, 0
        while mail_to_add_number < number_of_messages and mail_number_in_user_box < len(user_box):
            if not user_box[mail_number_in_user_box].read:
                return_box.append(user_box[mail_number_in_user_box].body)
                user_box[mail_number_in_user_box].read = True
                mail_to_add_number = mail_to_add_number + 1
            mail_number_in_user_box = mail_number_in_user_box + 1
        return return_box

    def search_inbox(self, user_name: str, string: str) -> list:
        messages_with_the_string = []
        user_box = self.boxes[user_name]
        for mail in user_box:
            if string in mail.body:
                messages_with_the_string.append(mail)
        return messages_with_the_string
