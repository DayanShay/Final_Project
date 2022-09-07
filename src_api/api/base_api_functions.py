import requests


def get_session(headers):
    sesion__ = requests.session()
    sesion__.headers.update(headers)
    return sesion__


def put(url=None, param=None):
    def formator(func, **kwargs):
        def convertor(self, *args, **kwargs):
            data = kwargs['data'] if 'data' in kwargs else None
            param_ = kwargs[param] if param else ""
            url_ = self._base_url + url if url else self._base_url
            response = self._session.put(url=url_ + param_, data=data)
            return func(self, response=response)
        return convertor
    return formator


def get(url=None, param=None):
    def formator(func, **kwargs):
        def convertor(self, *args, **kwargs):
            data = kwargs['data'] if 'data' in kwargs else None
            param_ = kwargs[param] if param else ""
            url_ = self._base_url + url if url else self._base_url
            response = self._session.get(url=url_ + param_, data=data)
            return func(self, response=response)
        return convertor
    return formator


def post(url=None, param=None):
    def formator(func, **kwargs):
        def convertor(self, *args, **kwargs):
            data = kwargs['data'] if 'data' in kwargs else None
            param_ = kwargs[param] if param else ""
            url_ = self._base_url + url if url else self._base_url
            response = self._session.post(url=url_ + param_, json=data)
            return func(self, response=response)
        return convertor
    return formator


def delete(url=None, param=None):
    def formator(func, **kwargs):
        def convertor(self, *args, **kwargs):
            data = kwargs['data'] if 'data' in kwargs else None
            param_ = kwargs[param] if param else ""
            url_ = self._base_url + url if url else self._base_url
            response = self._session.delete(url=url_ + param_, json=data)
            return func(self, response=response)
        return convertor
    return formator


def res_dict(code, msg):
    return {"code": code, "msg": msg}
