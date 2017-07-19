""" This module will be used to store create credentials specific account"""
from app.models.store import Stores
class Register(object):
    """ class that handles registration of accounts on bucketbook."""
    def __init__(self, firstname, lastname, email, password, index):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.index = index

    def register_stores(self):
        """returns information to be in the stores for credentials """
        return{
            'firstName': self.firstname,
            'lastName': self.lastname,
            'email': self.email,
            'password': self.password,
            'index': self.index,
            }
    def account_exists(self, auth_email):
        """ should check if the account exists and return the email with output messsage"""
        for email in len(Stores.account_store[2]):
            auth_email = Stores.account_store.pop(email)
            print ("Account exits, Login to account", auth_email)




    @classmethod
    def register_credentials(self, firstName, lastName, email, password, index):
        """ save account to a variable """
        new_account = self(firstName, lastName, email, password, index)
        new_account.save_credentials()

    def save_credentials(self):
        """ sends account to main store of accounts[account_store] """
        Stores.account_store.append(self.register_stores())
        