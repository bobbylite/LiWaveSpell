from liwavespellapplication.services.web.rest import WebRequest
from liwavespellapplication.api.keys import MagicSeaWeedKey

class MSW_WebRequest(WebRequest):
    __apiKey = MagicSeaWeedKey
    
    def Initialize(self):
        self.__urlWithKey = self._url.format(self.__apiKey)
        print(self.__urlWithKey)
    
