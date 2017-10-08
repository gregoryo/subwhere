"""
External vendor libraries
"""


import logging

from google.appengine.ext import vendor


try:
    vendor.add('lib')
except:  # pylint: disable=bare-except
    logging.warning('Unable to import lib directory')

