class repository:
    """Storage for user sign up"""

    _data_bank = {}

    def __init__(self):
        pass

    def save_data(self, email, name, password):
        name_pass_list = [name, password]
        self._data_bank[email] = name_pass_list
        return self._data_bank

    def get_data(self):
        return self._data_bank

    def search_data(self, email, password):
        if self._data_bank.__contains__(email):
            print(self._data_bank[email][1])
            print(password)
            if self._data_bank[email][1] == password:
                print("yea")
                return True
            else:
                print("nope")
        else:
            print("This email {} is incorrect".format(email))
            return False
