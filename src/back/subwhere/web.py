"""
Main application program
"""


import json
import logging

import webapp2

from subwhere.model import Greeting


class MainPage(webapp2.RequestHandler):
    """
    Main entry point for subwhere
    """
    def get(self):
        self.response.headers['Content-Type'] = 'text/json'
        results = list()
        for greeting in Greeting.query_by_content('World'):
            results.append('Hello {}'.format(greeting.content))
        self.response.write(json.dumps(results))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
