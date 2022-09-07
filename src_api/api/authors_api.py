from src_api.api.base_api import BaseApi
from src_api.api import base_api_functions as API_Func
from src_api.models.auth_response_dto import AuthResponseDto
from src_api.models.author import Author
from src_api.models.author_dto import AuthorDto
from src_api.models.get_author_dto import GetAuthorDto


class Authors_Api(BaseApi):
    def __init__(self, url: str, headers):
        super().__init__(url, headers)

    @API_Func.get(url="api/Authors")
    def get_authors(self, response):
        if response.ok:
            authors = []
            for author in response.json():
                authors.append(GetAuthorDto(**author))
            return authors
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.post(url="api/Authors")
    def post_authors(self,response):
        if response.ok:
            return Author(**response.json())
        return API_Func.res_dict(response.status_code,response.text)

    @API_Func.get(url=f"api/Authors")
    def get_authors_by_id(self, response):
        if response.ok:
            authdto = []
            for authdtos in response.json():
                authdto.append(AuthorDto(**authdtos))
            return authdto
        return API_Func.res_dict(response.status_code, response.text)




