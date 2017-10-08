"""
Subwhere model classes: communication with datastore on GCP
"""


from google.appengine.ext import ndb


class Greeting(ndb.Model):
    """
    Just a test
    """
    content = ndb.StringProperty()
    
    @classmethod
    def query_by_content(self, cnt):
        return self.query(Greeting.content == cnt)
        
