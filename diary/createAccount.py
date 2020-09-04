from Verifier import Verify


class SignUp:
    """Sign up functionality

        It is required that users have login credentials
        to enable them have private access to their diary.
    """

    def __init__(self, name, email, password):
        """Initializer of instance"""
        self.password = password
        self.name = name
        self.email = email
        self.save = Verify()

    def get_name(self):
        """Returns an instance of name"""
        return self.name

    def get_email(self):
        """Returns an instance of email"""
        self.save.email_validate(self.email)
        return self.email

    def get_password(self):
        """Returns an instance of hashed password"""
        self.password = self.save.secure_password(self.password)
        return self.password

    def save_details(self):
        """Saves sign up details into verify class"""
        self.save.save_signUp_details(self.email, self.name, self.password)

    def __str__(self) -> str:
        return "{} {} {}".format(self.get_name(), self.get_email(), self.get_password())
