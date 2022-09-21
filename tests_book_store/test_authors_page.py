from functions_and_fixtures.fixtures import *
from functions_and_fixtures.fixture_data import *
from functions_and_fixtures.functions import *

@pytest.mark.order(2)
class Test_authors_page_features:
    def test_contant_of_authors_page(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_from_api = api.authors.get_authors()
        authors_from_web = authors_page.get_author_container()

        assert len(authors_from_api) == len(authors_from_web)
        for index in range(len(authors_from_web)):
            author_name_web = authors_page.get_author_name(authors_from_web[index])
            author_name_api = authors_from_api[index].name
            assert author_name_web == author_name_api

    def test_go_to_author_page(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_from_web = authors_page.get_author_container()
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_from_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == last_author_from_api.name

    def test_contant_of_authors_page_after_post(self, get_to_main_page, get_api_UnAutho, create_authors_dto):
        page = get_to_main_page
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        author = create_authors_dto
        api.authors.post_authors(data=author)
        authors_page = page.click_authors_button()
        authors_page.page_refrash()
        authors_from_web = authors_page.get_author_container()
        last_author_from_web = authors_from_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == author.name

    def test_contant_of_authors_page_after_put(self, get_to_main_page, get_api_UnAutho):
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        last_author_from_api.name = "Sela Incorporation"
        api.authors.put_authors_by_id(data=last_author_from_api, id=last_author_from_api.id)
        page = get_to_main_page
        authors_page = page.click_authors_button()
        authors_page.page_refrash()
        authors_from_web = authors_page.get_author_container()
        last_author_from_web = authors_from_web[-1]
        name_on_authors_page = authors_page.get_author_name(last_author_from_web)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        name_on_author_page = author_page.get_author_name_top()
        assert name_on_author_page == name_on_authors_page == last_author_from_api.name

    def test_contant_of_authors_page_after_delete(self, get_to_main_page, get_api_UnAutho):
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        page = get_to_main_page
        authors_page = page.click_authors_button()
        authors_from_web_before = authors_page.get_author_container()
        last_author_from_web_before = authors_from_web_before[-1]
        api.authors.delete_authors_by_id(id=last_author_from_api.id)
        authors_page.page_refrash()
        authors_from_web_after = authors_page.get_author_container()
        last_author_from_web_after = authors_from_web_after[-1]
        assert last_author_from_web_before not in authors_from_web_after
        assert last_author_from_web_after != last_author_from_web_before
        delete_all_authors_and_books_created(api)
