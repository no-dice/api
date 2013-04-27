"""
Python interface to the No-Dice.net API
---------------------------------------

A simple library to interact with the No-Dice.Net API.
This module handles the Dice API.
"""

import requests
import json
import BaseHTTPServer
import SocketServer
from requests_oauth2.oauth2 import OAuth2
from . import api_url

class AuthHTTPServer(BaseHTTPServer):
    def do_GET(self):
        print "GET request"
        return None

class Die:
    _url_suffix = 'dice/die'
    
    def __init__(self):
        oauth = OAuth2('50e2b03a91f57cc088db', '2c9b63511aaee4c391a9f9816ee65f2422ff746c', 'http://no-dice.net/', 'http://no-dice.net/oauth2/authorize', 'oauth2/authorize', 'oauth2/access_token')
        http_handler = BaseHTTPServer.BaseHTTPRequestHandler
        http_server = SocketServer.TCPServer(("", 8000), http_handler)
        return None

    def set_suffix(self, suffix):
        _url_suffix = suffix

    def url(self):
        return ''.join([api_url(), self._url_suffix])

    def test(self):
        response = requests.get(self.url())
        return [self.url(), response.json()]
