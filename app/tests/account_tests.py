""" contains tests for methods of bucketbook app"""
import unittest
from app.models.user import User
from app.models.store import Stores
from app.models.bucketlist import Bucketlist
from app.models.activities import Activities


class TestAccount(unittest.TestCase):
    """ sets up TestAccount for testing methods"""
    def setUp(self):
        """ sets defaults to the test account"""
        self.store = Stores()
        self.dummy_user = {'username': 'hitchs3x',
                           'email': 'hitch@gmail.com',
                           'password': 'say123#',}
        self.dummy_bucketlist = {'bucketname': 'Before 2017 ends?',
                                 'bucket_id': '0'}
        self.dummy_activity = {'activitytxt': 'Buy early bird FIFA World Cup 2017 tickets'}
        del self.store.account_store[:]
        del self.store.bucketlist_store[:]
        del self.store.activities_store[:]
    def test_user_registration(self):
        """ checks if test can append to the register central store [account_store] """
        new_user = User.register_user('hitchs3x', 'hitch@gmail.com', 'say123#')
        self.assertEqual(new_user.email, 'hitch@gmail.com')    
    def test_create_bucketlist(self):
        """" check if dummy_bucket can append to the central store [bucketlist_store]"""
        dummy_bucketlist = self.store.bucketlist_store.append(self.dummy_bucketlist)
        new_bucket = Bucketlist.create_bucketlist('Before 2017 ends?', '0')
        assert new_bucket == dummy_bucketlist
    def test_create_activity(self):
        """" check if dummy_actvity can append to the central store [activity_store]"""
        dummy_activity = self.store.activities_store.append(self.dummy_activity)
        new_activity = Activities.create_activity('Buy early bird FIFA World Cup 2017 tickets', '0')
        assert new_activity == dummy_activity
    def test_account_exists(self):
        """ tests if user exists and passes tesst if true"""
        new_user = User.register_user('hitchs3x', 'hitch@gmail.com', 'say123#')
        new_user = User.register_user('hitchs3x', 'hitch@gmail.com', 'say123#')  
        self.assertEqual(new_user, new_user)     
