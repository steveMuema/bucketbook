from register import Register
from bucketlist import Bucketlist
from activities import Activities
class Account(object):
    """Account """
    def __init__(self, firstName, lastName, email, password, index, txtbucket, txtActivity):
        """ initializes the credentials of user"""
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.index=index
        self.txtbucket=txtbucket
        self.txtActivity=txtActivity

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

    def create_activity(self, txtActivity):
        """inherits from bucketlist"""
        activity= Activities(
            txtActivity = txtActivity
        )