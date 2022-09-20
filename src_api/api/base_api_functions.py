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


def bad_respone_msg(code, msg):
    return {"code": code, "msg": msg}

