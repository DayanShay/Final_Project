import requests
from src_api.api_models import *

class Api():
    def __init__(self, url: str, headers):
        self._session = requests.session()
        self._account = Account_Api(url, headers, self._session)
        self._authors = Authors_Api(url, headers, self._session)
        self._books = Books_Api(url, headers, self._session)

    def update_session_header(self, headers):
        self._session.headers.update(headers)

    @property
    def session(self):
        return self._session

    @property
    def account(self):
        return self._account

    @property
    def authors(self):
        return self._authors

    @property
    def books(self):
        return self._books
