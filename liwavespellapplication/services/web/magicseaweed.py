from liwavespellapplication.services.web.rest import WebRequest
from liwavespellapplication.api.keys import MagicSeaWeedKey

class MSW_WebRequest(WebRequest):
    __apiKey = MagicSeaWeedKey

    def __init__(self, url):
        self._url = url
        self.InitializeKey()
    
    def InitializeKey(self):
        urlWithKey = self._url.format(self.__apiKey)
        self._url = urlWithKey
    
    def Clean_datetime(self, json):
        try:
            pass
        except:
            return {'error': 'could not cleanup datetimes.'}