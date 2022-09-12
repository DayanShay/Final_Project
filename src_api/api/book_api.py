from src_api.api.base_api import BaseApi
from src_api.api import base_api_functions as API_Func
from src_api.models.book import Book
from src_api.models.book_dto import BookDto


class Books_Api(BaseApi):
    def __init__(self, url: str, headers):
        super().__init__(url, headers)

    @API_Func.make_a_req(url="api/Books", action="get")
    def get_books(self, response):
        if response.ok:
            books = []
            for book in response.json():
                books.append(BookDto(**book))
            return books
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Books", action="post")
    def post_books(self, response):
        if response.ok:
            return Book(**response.json())
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Books/", action="get", param="id")
    def get_books_by_id(self, response):
        if response.ok:
            return BookDto(**response.json())
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Books/", action="put", param="id")
    def put_books_by_id(self, response):
        if response.ok:
            return response.json()
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Books/", action="delete", param="id")
    def delete_books_by_id(self, response):
        if response.ok:
            return response.text
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Books/findauthor/", action="get", param="authorid")
    def get_books_by_author_id(self, response):
        if response.ok:
            books = []
            for book in response.json():
                books.append(BookDto(**book))
            return books
        return API_Func.res_dict(response.status_code, response.text)

    @API_Func.make_a_req(url="api/Books/purchase/", action="put", param="id")
    def put_purchese_by_books_id(self,response):
        if response.ok:
            return Book(**response.json())
        return API_Func.res_dict(response.status_code, response.text)

