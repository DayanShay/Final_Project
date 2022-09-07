from src_api.api import base_api_functions as API_Func

class BaseApi:
    def __init__(self,url:str,headers):
        self._base_url = url
        self._headers = headers
        self._session = API_Func.get_session(self._headers)
