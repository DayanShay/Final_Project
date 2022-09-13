from src_api.api.base_api import BaseApi
from src_api.api import base_api_functions as API_Func
from src_api.models.auth_response_dto import AuthResponseDto
from src_api.models.author import Author
from src_api.models.author_dto import AuthorDto
from src_api.models.get_author_dto import GetAuthorDto
from src_api.models.update_author_dto import UpdateAuthorDto


class Authors_Api(BaseApi):
    def __init__(self, url: str, headers):
        super().__init__(url, headers)

    @API_Func.make_a_req(url="api/Authors",action= "get")
    def get_authors(self, response):
        if response.ok:
            authors = []
            for author in response.json():
                authors.append(GetAuthorDto(**author))
            return authors
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Authors", action="post")
    def post_authors(self,response):
        if response.ok:
            return Author(**response.json())
        return API_Func.res_dict(response.status_code,response.text)

    @API_Func.make_a_req(url=f"api/Authors/",action="get",param="id")
    def get_authors_by_id(self, response):
        if response.ok:
            return AuthorDto(**response.json())
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url=f"api/Authors/",action="put",param="id")
    def put_authors_by_id(self, response):
        if response.ok:
            return None
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url=f"api/Authors/",action="delete",param="id")
    def delete_authors_by_id(self, response):
        if response.ok:
            return response.text
        return response.text


    @API_Func.make_a_req(url=f"api/Authors/search/",action="get",param='text')
    def search_authors_by_text(self, response):
        if response.ok:
            authors = []
            for author in response.json():
                authors.append(GetAuthorDto(**author))
            return authors
        return response.text




