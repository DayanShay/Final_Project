from tests.fixture_restapi import *

class Test_author_page_features:

    def test_author_map_locations(self,get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_from_api = api.authors.get_authors()
        authors_from_web = authors_page.get_author_container()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_from_web[-1]
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        homeLatitude, homeLongitude = author_page.get_home_location()
        assert round(last_author_from_api.homeLatitude,4) == homeLatitude
        assert round(last_author_from_api.homeLongitude,4) == homeLongitude

    def test_author_page_contant_of_books(self,get_to_main_page, get_api_UnAutho):
        pass

    def test_author_page_contant_of_books_after_post(self,get_to_main_page, get_api_UnAutho):
        pass
    def test_author_page_contant_of_books_after_put(self,get_to_main_page, get_api_UnAutho):
        pass
    def test_author_page_contant_of_books_after_delete(self,get_to_main_page, get_api_UnAutho):
        pass