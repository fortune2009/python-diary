import bcrypt
from Verifier import Verify
from database import repository


class LogIn:
    """Log in functionality"""

    def __init__(self, email, password):
        """Initialization"""
        self.email = email
        self.password = password
        self.hashed = False
        self.hash = Verify()
        self.data = ''

    def verify_credentials(self):
        # print(self.password)
        self.hashed = self.hash.match_password(self.password)
        return self.hashed

    def __str__(self) -> str:
        return super().__str__()
