import requests


class BaseApi:
    def __init__(self,url:str,headers,session):
        self._base_url = url
        self._headers = headers
        self._session = session

    def select_session_req(self, action):
        actions = {"post": self._session.post,
                   "put": self._session.put,
                   "get": self._session.get,
                   "delete": self._session.delete}
        return actions[action]

    def update_session_header(self, headers):
        self._session.headers.update(headers)



    @staticmethod
    def make_a_req(url=None, param=None, action=None):
        def formator(func, **kwargs):
            def convertor(self, *args, **kwargs):
                data = kwargs['data'].to_json() if 'data' in kwargs else None
                param_ = kwargs[param] if param else ""
                url_ = self._base_url + url if url else self._base_url
                req_action = self.select_session_req(action)
                response = req_action(url=url_ + f"{param_}", json=data)
                return func(self, response=response)

            return convertor

        return formator
