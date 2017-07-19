from register import Register
from bucketlist import Bucketlist
class Account(object):
    """Account """
    def __init__(self, firstName, lastName, email, password, index, txtbucket):
        """ initializes the credentials of user"""
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.index=index
        self.txtbucket=txtbucket

    def account_credentials(self, firstName, lastName, email, password,index):
        """ inherits attributes from register"""
        credentials = Register(
            firstName = firstName,
            lastName = lastName,
            email = email,
            password = password,
            index=index,
        )
        return credentials 
         
    def create_bucketlist(self, txtbucket):
        """inherits from bucketlist"""
        bucketlist= Bucketlist(
            txtbucket = txtbucket
        )
        return bucketlist