import requests
from enum import Enum
import sys

class WebRequest:

    def __init__(self, url):
        self._url = url
    
    def post(self, data_object):
        try:
            response = requests.post(self._url, data_object)
            null_or_empty = None == response
            return {'error': 'empty response'} if null_or_empty else response
        except:
            return {'request error': sys.exc_info()[0]}

    def get(self):
        try:
            response = requests.get(self._url)
            null_or_empty = None == response
            return {'error': 'empty response'} if null_or_empty else response
        except:
            return {'request error': sys.exc_info()[0]}

    @staticmethod
    def parse(response):
        try:
            null_or_empty = None == response
            return {'error': 'cannot parse empty response'} if null_or_empty else response.json()
        except:
            return {'error': sys.exc_info()[0]}


class parse_TYPE(Enum):
    """
        Enum for WebRequest.parse_JSON(parse_TYPE.x, response) method.
    """
    JSON = 1
    TEXT = 2