from liwavespellapplication.services.web.rest import WebRequest
from liwavespellapplication.api.keys import MagicSeaWeedKey
import datetime, sys

class MSW_WebRequest(WebRequest):
    __apiKey = MagicSeaWeedKey

    def __init__(self, url):
        self._url = url
        self.InitializeKey()
    
    def InitializeKey(self):
        urlWithKey = self._url.format(self.__apiKey)
        self._url = urlWithKey

    @staticmethod
    def Clean_Datetime(json):
        try:
            for timestamp in json:
                timestamp_data = timestamp['localTimestamp']
                date = datetime.datetime.utcfromtimestamp(timestamp_data)
                timestamp['localTimestamp'] = date
            null_or_empty = None == json 
            return {'error': 'cannot parse empty response'} if null_or_empty else json
        except:
            return {'Clean_datetime Error': sys.exc_info()[0]}