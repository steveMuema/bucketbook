from store import Stores

class Register(object):
    def __init__(self, firstName, lastName, email, password, index):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.index=index

    def register_stores(self):
        """returns information to be in the stores for credentials """
        return{
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'password': self.password,
            'index': self.index,
            }
    
    # def account_exists(self):
    #     for x in register_credentials(email):




    @classmethod
    def register_credentials(self, firstName, lastName, email, password, index):

        new_account= self(firstName, lastName, email, password, index)
        new_account.save_credentials()

    def save_credentials(self):
        Stores.account_store.append(self.register_stores())

    
        