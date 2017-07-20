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
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'password': self.password,
            'index': self.index,
            }
    # def account_exists(email):
    #     """ should check if the account exists and return the email with output messsage"""
    #     account_exist= [e['email'] for e in Stores.account_store if email == e['email']]:
    #         return ''.join(account_exist)==email
    @classmethod
    def register_credentials(cls, firstname, lastname, email, password, index):
        """ save account to a variable """
        new_account_store = cls(firstname, lastname, email, password, index)
        #append it to stores
        new_account_store.save_credentials()
    def save_credentials(self):
        """ sends account to main store of accounts[account_store] """
        Stores.account_store.append(self.register_stores())
        
        