import requests


def get_session(headers):
    sesion__ = requests.session()
    sesion__.headers.update(headers)
    return sesion__


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


def res_dict(code, msg):
    return {"code": code, "msg": msg}

# def put(url=None, param=None):
#     def formator(func, **kwargs):
#         def convertor(self, *args, **kwargs):
#             data = kwargs['data'] if 'data' in kwargs else None
#             param_ = kwargs[param] if param else ""
#             url_ = self._base_url + url if url else self._base_url
#             response = self._session.put(url=url_ + param_, data=data)
#             return func(self, response=response)
#         return convertor
#     return formator
#
#
# def get(url=None, param=None):
#     def formator(func, **kwargs):
#         def convertor(self, *args, **kwargs):
#             data = kwargs['data'] if 'data' in kwargs else None
#             param_ = kwargs[param] if param else ""
#             url_ = self._base_url + url if url else self._base_url
#             response = self._session.get(url=url_ + param_, data=data)
#             return func(self, response=response)
#         return convertor
#     return formator
#
#
# def post(url=None, param=None):
#     def formator(func, **kwargs):
#         def convertor(self, *args, **kwargs):
#             data = kwargs['data'] if 'data' in kwargs else None
#             param_ = kwargs[param] if param else ""
#             url_ = self._base_url + url if url else self._base_url
#             response = self._session.post(url=url_ + param_, json=data)
#             return func(self, response=response)
#         return convertor
#     return formator
#
#
# def delete(url=None, param=None):
#     def formator(func, **kwargs):
#         def convertor(self, *args, **kwargs):
#             data = kwargs['data'] if 'data' in kwargs else None
#             param_ = kwargs[param] if param else ""
#             url_ = self._base_url + url if url else self._base_url
#             response = self._session.delete(url=url_ + param_, json=data)
#             return func(self, response=response)
#         return convertor
#     return formator
# def make_a_req(url=None, param=None,action=None):
#     def formator(func, **kwargs):
#         def convertor(self, *args, **kwargs):
#             data = kwargs['data'] if 'data' in kwargs else None
#             json = kwargs['json'] if 'json' in kwargs else None
#             param_ = kwargs[param] if param else ""
#             url_ = self._base_url + url if url else self._base_url
#             if action:
#                 response = self._session(action,url=url_ + param_, data=data,json=json)
#             return func(self, response=response)
#         return convertor
#     return formator
# def select_session_req(self,action=None):
#     actions = {"post":self._session.post,
#                "put":self._session.put,
#                "get":self._session.get,
#                "delete":self._session.delete}
#     if action:
#         return actions["action"]
#     raise AttributeError(f"session request not supports that kind of action {action}")
