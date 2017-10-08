"""
Main application program
"""


import json
import logging

import webapp2

import subwhere.config
from subwhere.model import UserData


logger = logging.getLogger('api-user')


class UsersHandler(webapp2.RequestHandler):
    """
    Main entry point for subwhere
    """
    def get(self):
        """
        Get all the data from the backend
        """
        # TODO: add some filters from the get
        self.response.headers['Content-Type'] = 'text/json'
        results = list()
        
        id = self.request.get('id', None)
        if id is not None:
            results.append(UserData.get_by_id(id=int(id)).to_json())
        else:
            query = UserData.query()
            types = self.request.get('types', None)
            if types is not None:
                query.filter(UserData.type.IN(types.split(',')))
            for data in query:
                results.append(data.to_json())
        self.response.write(json.dumps(results))

    def post(self):
        """
        Create a new entity
        """
        # TODO: manage errors
        self.response.headers['Content-Type'] = 'text/json'
        UserData.create_from_json(json.loads(self.request.body))

class EventHandler(webapp2.RequestHandler):
    """
    Confirm or deny an event. The method (confirm or deny) and id of the event
    must be provided
    """
    def post(self, method, id):
        """
        Post method to confirm or deny
        """
        data = UserData.get_by_id(id=int(id))
        if method == 'confirm':
            data.confirmed += 1
        elif method == 'deny':
            data.denied += 1
        data.put()

app = webapp2.WSGIApplication([
    ('/api/users$', UsersHandler),
    ('/api/users/(confirm|deny)/([1-9][0-9]*)$', EventHandler)
], debug=True)
