from Verifier import Verify
from createAccount import SignUp
from accessAccount import LogIn

if __name__ == "__main__":
    # -----Prompt for user input----- #
    # name = input("Enter Name-> ")
    # email = input("Enter Email-> ")
    # password = input("Enter password-> ")

    # -----String variables for testing----- #
    name: str = "John Gue"
    email: str = "john@doe.com"
    password: str = "free"

    # -----Sign up instance, initializer and class Verify for validation/ hashing----- #
    createAccount = SignUp(name, email, password)
    very = Verify()
    try:
        very.email_validate(email)
        print(createAccount.__str__())
    except ValueError as e:
        print(e)

    # -----Save account details and query----- #
    createAccount.save_details()
    # print(very.data.get_data())

    # -----Log in instance and class ----- #
    password1 = "free"
    logIn = LogIn(email, password1)
    print(logIn.verify_credentials())
    # very.match_password(password1)

    # print(logIn.__str__())
