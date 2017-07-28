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
        self.dummy_user = {'username': 'hitch',
                           'email': 'hitch@gmail.com',
                           'password': 'say123#', 
                           'user_id': 'vbhvghv',}
        self.dummy_bucketlist = {'bucketname': 'Before 2017 ends?',
                                 'bucket_id': '0'}
        self.dummy_activity = {'activitytxt': 'Buy early bird FIFA World Cup 2017 tickets'}
        del self.store.account_store[:]
        del self.store.bucketlist_store[:]
        del self.store.activities_store[:]
    def test_user_registration(self):
        """ checks if test can append to the register central store [account_store] """
        new_user = User.register_user('hitch', 'hitch@gmail.com', 'say123#', 'vbhvghv')
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
        self.assertEqual(dummy_activity, new_activity)
    def test_account_exists(self):
        """ tests if user exists and passes tesst if true"""
        new_user = User.account_exists('hitch')
        new_user1 = User.account_exists('hitch')  
        self.assertEqual(new_user, new_user1)     

    def test_bucketlist_filled(self):
        """ test if bucketlist is empty"""
        newbucketlist=Bucketlist.create_bucketlist('', '')
        print(newbucketlist)
        self.assertEqual(newbucketlist, None, msg="You must write something")

    def test_activity_filled(self):
        """ test if activity is empty """
        newActivity=Activities.create_activity('', '')
        print(newActivity)
        self.assertEqual(newActivity, None, msg="You must write something")
    
    def test_username_exists(self):
        new_user=User.username_exists('hitch')
        new_user1=User.username_exists('hitch')
        self.assertEqual(new_user, new_user1)