from tests.functions_and_fixtures.fixtures import *
from tests.functions_and_fixtures.fixture_data import *
from tests.functions_and_fixtures.functions import *

@pytest.mark.order(4)
class Test_search_page_features:
    def test_search_empty_text(self,get_to_main_page,get_base_url):
        page = get_to_main_page
        api = get_api_UnAutho
        page.fill_serch_text()
        search_page = page.click_search()
        page_url = search_page.get_page_url()
        assert page_url == f"{get_base_url}search"
        authors = search_page.get_author_container()
        assert len(authors) == 0
        books = search_page.get_book_container()
        assert len(books) == 0

    def test_search_empty_text_click_search_twice(self,get_to_main_page,get_base_url):
        page = get_to_main_page
        page.fill_serch_text()
        search_page = page.click_search()
        search_page = search_page.click_search()
        page_url = search_page.get_page_url()
        assert page_url == f"{get_base_url}search"
        authors = search_page.get_author_container()
        assert len(authors) == 0
        books = search_page.get_book_container()
        assert len(books) == 0

    def test_search_after_post_author(self,get_to_main_page,get_api_UnAutho,create_authors_dto,get_base_url):
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        author = create_authors_dto
        res_post_author = api.authors.post_authors(data=author)
        page = get_to_main_page
        page.page_refrash()
        page.fill_serch_text(res_post_author.name)
        search_page = page.click_search()
        page_url = search_page.get_page_url()
        last_authors_web = search_page.get_author_container()[-1]
        author_name = search_page.get_author_name(last_authors_web)
        assert author_name == res_post_author.name
        assert page_url == f"{get_base_url}search"

    def test_search_by_author_name_twice_clicked(self,get_to_main_page,get_api_UnAutho,create_authors_dto,get_base_url):
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        author = create_authors_dto
        page = get_to_main_page
        page.page_refrash()
        page.fill_serch_text(author.name)
        page.click_search()
        search_page = page.click_search()
        page_url = search_page.get_page_url()
        last_authors_web = search_page.get_author_container()[-1]
        author_name = search_page.get_author_name(last_authors_web)
        books_web = search_page.get_book_container()
        delete_all_authors_and_books_created(api)
        assert author_name == author.name
        assert len(books_web) == 0
        assert page_url == f"{get_base_url}search"
        delete_all_authors_and_books_created(api)
