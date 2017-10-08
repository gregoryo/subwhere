# -*- coding: utf-8 -*-
"""
Subwhere model classes: communication with datastore on GCP
"""

from datetime import datetime as dt
import logging
import math

from google.appengine.ext import ndb

from subwhere.helpers import clean_json_type


logger = logging.getLogger('api-model')


class UserData(ndb.Model):
    """
    User data gathered from interface
    """
    event_datetime = ndb.DateTimeProperty(auto_now_add=True)
    lat = ndb.FloatProperty(required=True)
    lon = ndb.FloatProperty(required=True)
    type = ndb.StringProperty(
        required=True,
        choices=[
            'Delay',
            'Cancellation', 
            'Slowed traffic', 
            'Inability to climb up', 
            'Musician', 
            'Fight', 
            'Pretty woman', 
            'Awesome dude', 
            'Bad smell'
        ]
    )
    comment = ndb.StringProperty(indexed=False)
    expiration_datetime = ndb.DateTimeProperty()
    confirmed = ndb.IntegerProperty(default=1)
    denied = ndb.IntegerProperty(default=0)

    @classmethod
    def _get_kind(cls):
        return 'UserData'

    @staticmethod
    def get_by_id(id):
        key = ndb.Key(UserData, id)
        return key.get()

    def to_json(self):
        """
        Send back a valid json representation of the data
        """
        data = clean_json_type(self.to_dict())
        data['id'] = self.key.pairs()[0][1]
        return data
    
    @staticmethod
    def create_from_json(json_info):
        """
        Build a uset data from a json_information
        """
        # TODO: manage exception

        # Check arguments
        args = dict()

        if 'event_datetime' in json_info and \
                json_info['event_datetime']:
            args['event_datetime'] = dt.strptime(
                json_info['event_datetime'],
                '%Y-%m-%d %H:%M:%S'
            )

        latitude = float(json_info['lat'])
        if math.isnan(latitude) or math.isinf(latitude) \
                or not -90.0 <= latitude <= 90.0:
            raise ValueError(
                'Get an invalid latitude. Latitude must be a float between '\
                '-90° and 90°'
            )
        args['latitude'] = latitude

        longitude = float(json_info['lon'])
        if math.isnan(longitude) or math.isinf(longitude) \
                or not -180.0 <= longitude <= 180.0:
            raise ValueError(
                'Get an invalid longitude. Longitude must be a float between '\
                '-180° and 180°'
            )
        args['longitude'] = longitude
        
        args['type'] = json_info['type']
        
        args['comment'] = json_info['comment']

        if 'expiration_datetime' in json_info and \
                json_info['expiration_datetime']:
            args['expiration_datetime'] = dt.strptime(
                json_info['expiration_datetime'],
                '%Y-%m-%d %H:%M:%S'
            )


        # Create the entity
        entity = UserData()
        entity.populate(**args)
        
        return entity.put()
