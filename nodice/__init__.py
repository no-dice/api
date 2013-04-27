"""
Python interface to the No-Dice.net API
---------------------------------------

A simple library to interact with the No-Dice.Net API.
"""

__title__ = 'nodice'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'T. Scott Barnes'
__license__ = 'BSD'
__copyright__ = 'Copyright 2013 No Dice, LLC'

class NoDiceAPI:
    _api_url = "http://no-dice.net/api/"
    
    def __init__(self):
        return None

    @classmethod
    def url(cls, new_url=None):
        if new_url != None:
            cls._api_url = new_url
        return cls._api_url

def api_url(new_url=None):
    return NoDiceAPI.url(new_url)

import logging
try: # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
