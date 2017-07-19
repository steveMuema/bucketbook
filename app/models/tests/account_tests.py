import unittest
from app.models.register import Register
from app.models.store import Stores

class TestAccount(unittest.TestCase):


    def setUp(self):
        """ sets defaults to the test account"""
        self.store=Stores()
        self.dummy_account = {  'firstName': 'Alec',
                                'lastName': 'Hitch',
                                'email': 'hitch@gmail.com',
                                'password': 'say123#',
                                'index':'12002'}    
        
        del self.store.account_store[:]

    def test_registration(self):
        """ checks if test can append to the register central store [account_store] """
        dummy_account=self.store.account_store.append(self.dummy_account)
        new_account= Register.register_credentials('Alec', 'Hitch', 'hitch@gmail.com', 'say123#', '12002')
        assert new_account == dummy_account
        
    def test_create_bucketlist(self):


