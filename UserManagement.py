class UserManagement:
    """
    A user management class.
    """
    def __init__(self, user_name: str, password: str, kind: str):
        """
        Class constructor.
        :param user_name: The user Username.
        :param password: The user password.
        :param kind: System administrator or User.
        """
        self.user_name = user_name
        self.password = password
        self.kind = kind
