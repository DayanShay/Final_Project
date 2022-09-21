from src_api.api_models.base_api import BaseApi
from src_api.api_models import base_api_functions as API_Func
from src_api.obj_models.api_user_dto import ApiUserDto
from src_api.obj_models.auth_response_dto import AuthResponseDto
from src_api.obj_models.problem_details import ProblemDetails


class Account_Api(BaseApi):
    def __init__(self, url: str, headers,session):
        super().__init__(url, headers,session)

    @BaseApi.make_a_req(url="api_models/Account/register", action="post")
    def post_account(self,response):
        if response.ok:
            return response.reason
        return API_Func.bad_respone_msg(response.status_code, response.text)

    @BaseApi.make_a_req(url="api_models/Account/login", action="post")
    def post_login(self, response) -> AuthResponseDto:
        if response.ok:
            return AuthResponseDto(**response.json())
        return API_Func.bad_respone_msg(response.status_code, response.text)

    @BaseApi.make_a_req(url="api_models/Account/refreshtoken", action="post")
    def post_refresh_token(self, response):
        if response.ok:
            return AuthResponseDto(**response.json())
        return API_Func.bad_respone_msg(response.status_code, response.text)


