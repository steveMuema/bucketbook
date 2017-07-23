""" This module will be used to store create credentials specific account"""
from app.models.store import Stores
class User(object):
    """ class that handles registration of accounts on bucketbook."""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def register_stores(self):
        """returns information to be in the stores for credentials """
        return{
            'username': self.username,
            'email': self.email,
            'password': self.password,}
    @staticmethod
    def username_exists(username):
        """ Method to validate username registration"""
        exist = [e['username'] for e in Stores.account_store if username == e['username']] 
        return "Username not available".join(exist)
    @staticmethod   
    def account_exists(email):
        """ method to check if account exists then allow registration if false"""
        if email in Stores.account_store:
            return "Account exist, Sign in to account" 
        else:
            return False
    @classmethod
    def register_user(cls, username, email, password):
        """ method for creating a new user"""
        auth_user = User.account_exists(email)
        if auth_user is False:
            new_user = cls(username, email, password)
            new_user.save_credentials()
            return new_user
        else: return auth_user 
    def save_credentials(self):
        """ sends account to main store of accounts[account_store] """
        Stores.account_store.append(self.register_stores())
    # def login_user(cls, username, email, password):
            