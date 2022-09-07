from src_api.api.base_api import BaseApi
from src_api.api import base_api_functions as API_Func
from src_api.models.auth_response_dto import AuthResponseDto


class Account_Api(BaseApi):
    def __init__(self, url: str, headers):
        super().__init__(url, headers)

    @API_Func.post(url="api/Account/register")
    def post_account(self,response):
        if response.ok:
            return response.json()
        return API_Func.res_dict(response.status_code,response.text)

    @API_Func.post(url="api/Account/login")
    def login_account(self,response):
        if response.ok:
            return AuthResponseDto(**response.json())
        return API_Func.res_dict(response.status_code,response.text)

    @API_Func.post(url="api/Account/refreshtoken")
    def refresh_token(self,response):
        if response.ok:
            return AuthResponseDto(**response.json())
        return API_Func.res_dict(response.status_code,response.text)


