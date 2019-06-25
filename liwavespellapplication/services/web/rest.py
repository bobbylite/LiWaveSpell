import requests
from enum import Enum

class WebRequest:

    def __init__(self, url):
        self._url = url
    
    def post(self, data_object):
        try:
            response = requests.post(self._url, data_object)
            null_or_empty = None == response
            return {error: 'could not post'} if null_or_empty else response
        except:
            return {error: 'could not post'}

    def get(self):
        try:
            response = requests.get(self._url)
            null_or_empty = None == response
            return {error: 'could not get'} if null_or_empty else response
        except:
            return {error: 'could not get'}

    @staticmethod
    def parse_JSON(response):
        try:
            null_or_empty = None == response
            return {error: 'cannot parse empty response'} if null_or_empty else response.json()
        except:
            return {error: 'could not parse'}


class parse_TYPE(Enum):
    """
        Enum for WebRequest.parse_JSON(parse_TYPE.x, response) method.
    """
    JSON = 1
    TEXT = 2