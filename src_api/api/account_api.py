from src_api.api.base_api import BaseApi
from src_api.api import base_api_functions as API_Func
from src_api.models.api_user_dto import ApiUserDto
from src_api.models.auth_response_dto import AuthResponseDto
from src_api.models.problem_details import ProblemDetails


class Account_Api(BaseApi):
    def __init__(self, url: str, headers,session):
        super().__init__(url, headers,session)

    @BaseApi.make_a_req(url="api/Account/register", action="post")
    def post_account(self,response):
        if response.ok:
            return response.reason
        return API_Func.res_dict(response.status_code, response.text)

    @BaseApi.make_a_req(url="api/Account/login", action="post")
    def post_login(self, response) -> AuthResponseDto:
        if response.ok:
            return AuthResponseDto(**response.json())
        return API_Func.res_dict(response.status_code, response.text)

    @BaseApi.make_a_req(url="api/Account/refreshtoken", action="post")
    def post_refresh_token(self, response):
        if response.ok:
            return AuthResponseDto(**response.json())
        return API_Func.res_dict(response.status_code, response.text)


