"""
Configuration module for subwhere project
"""


import logging


DEFAULT_FORMAT = '[%(asctime)s - %(levelname)s] [%(name)s] %(message)s'
DEFAULT_LEVEL = 'DEBUG'
logging.basicConfig(level=DEFAULT_LEVEL, format=DEFAULT_FORMAT)
