from src_api.api import base_api_functions as API_Func

class BaseApi:
    def __init__(self,url:str,headers):
        self._base_url = url
        self._headers = headers
        self._session = API_Func.get_session(self._headers)

    def select_session_req(self, action=None):
        actions = {"post": self._session.post,
                   "put": self._session.put,
                   "get": self._session.get,
                   "delete": self._session.delete}
        if action:
            return actions[action]
        raise AttributeError(f"session request not supports that kind of action {action}")
