from app.models.store import Stores
# from app.models.bucketlist import Bucketlist

class Activities(object):
    def __init__(self, activitytxt):
        self.activitytxt = activitytxt
    def activity_stores(self):
        """return information to be called  when appending to the store"""
        return{'activitytxt': self.activitytxt}
    def view_activity(self):
        activity=Activities.activity_stores(self)
    @classmethod
    def new_activity(cls, activitytxt):
        """ sets the attribute of the class to new_activity and append on store"""
        new_activity = cls(activitytxt)
        if new_activity == "": 
            new_activity.new_buckets_activity()
        else: new_activity.save_activity()
   
    def new_buckets_activity(self):
       self.activitytxt = []
       self.activitytxt.save_activity()

    def save_activity(self):
        """ method for appending created txtbucket to the bucketlist_store on (central) store   """
        Stores.activities_store.append(self.activity_stores())

     def get_activities(self):
        view_activities = Stores.activities_store
        return view_activities