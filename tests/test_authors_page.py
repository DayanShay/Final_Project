from tests.fixture_restapi import *

class Test_authors_page_features:

    def test_contant_of_authors_page(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_form_api = api.authors.get_authors()
        authors_form_web = authors_page.get_author_container()

        assert len(authors_form_api) == len(authors_form_web)
        for index in range(len(authors_form_web)):
            author_name_web = authors_page.get_author_name(authors_form_web[index])
            author_name_api = authors_form_api[index].name
            assert author_name_web == author_name_api

    def test_go_to_author_page(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_form_web = authors_page.get_author_container()
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_form_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == last_author_from_api.name

    def test_contant_of_authors_page_after_post(self, get_to_main_page, get_api_UnAutho, create_authors_dto,
                                          get_create_book_dto):
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        page = get_to_main_page
        api = make_sesion_autho(get_api_UnAutho, user_login)
        authors_page = page.click_authors_button()
        authors_form_web = authors_page.get_author_container()
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_form_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == last_author_from_api.name

    def test_contant_of_authors_page_after_put(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_form_web = authors_page.get_author_container()
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_form_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == last_author_from_api.name

    def test_contant_of_authors_page_after_delete(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_form_web = authors_page.get_author_container()
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_form_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == last_author_from_api.name