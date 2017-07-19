import unittest
from app.models.register import Register
from app.models.store import Stores
from app.models.bucketlist import Bucketlist
from app.models.activities import Activities

class TestAccount(unittest.TestCase):


    def setUp(self):
        """ sets defaults to the test account"""
        self.store = Stores()
        self.dummy_account = {  'firstName': 'Alec',
                                'lastName': 'Hitch',
                                'email': 'hitch@gmail.com',
                                'password': 'say123#',
                                'index':'12002'}    
        
        self.dummy_bucketlist = {'txtbucket': 'Watch the FIFA World Cup 2018 live'}
        self.dummy_activity = {'txtActivity': 'Buy ticket early bird'}
        del self.store.account_store[:]
        del self.store.bucketlist_store[:]
        del self.store.activities_store[:]

    def test_registration(self):
        """ checks if test can append to the register central store [account_store] """
        dummy_account = self.store.account_store.append(self.dummy_account)
        new_account = Register.register_credentials('Alec', 'Hitch', 'hitch@gmail.com', 'say123#', '12002')
        assert new_account == dummy_account
        
    def test_create_bucketlist(self):
        """" check if dummy_bucket can append to the central store [bucketlist_store]"""
        dummy_bucketlist = self.store.bucketlist_store.append(self.dummy_bucketlist)
        new_bucket = Bucketlist.new_bucketlist('Watch FIFA World Cup 2018 live')
        assert new_bucket == dummy_bucketlist

    def test_create_activity(self):
        """" check if dummy_bucket can append to the central store [bucketlist_store]"""
        dummy_activity = self.store.activities_store.append(self.dummy_activity)
        new_activity = Activities.new_activity('Buy ticket early bird')
        assert new_activity == dummy_activity



    # def test_account_exists(self, auth_email):
    #     dummy_account = self.store.account_store.append(self.dummy_account)
    #     auth_email=Register.auth_email.account_exist('hitch@gmail.com')
    #     assert auth_email == dummy_account[2]
      

