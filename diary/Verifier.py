import re
import bcrypt
from database import repository


class Verify:
    email = ""

    def __init__(self):
        """Initializer of properties"""
        self.data = repository()
        self.hashed = bytes("".encode())
        self.DAO = {}
        self.valid_email = False
        self.email = ""

    def email_validate(self, email):
        """Email validation pattern"""
        pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
        if re.search(pattern, email):
            self.valid_email = True
            self.copy_email(email)
            return self.valid_email
        else:
            self.valid_email = False
            raise ValueError("{} <- is an invalid email format, Try again!".format(email))

    def copy_email(self, email):
        self.email = email
        return self.email

    def secure_password(self, password):
        hashing = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.hashed = hashing
        return self.hashed

    def hash(self):
        return self.hashed

    def match_password(self, password):
        # print(self.hashed)
        # print(self.data.get_data()[self.email][1])
        # print(self.data.get_data()[self.email])
        print(self.email)
        # if bcrypt.checkpw(password.encode("utf-8"), self.data.get_data()[self.email][1]):
        #     print("it matches")
        #     return True
        # else:
        #     print("didn't match")

    def save_signUp_details(self, email, name, password):
        DAO = self.data.save_data(email, name, password)
        self.DAO = DAO.copy()
        return self.DAO
