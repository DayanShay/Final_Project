from functions_and_fixtures.fixtures import *
from functions_and_fixtures.fixture_data import *
from functions_and_fixtures.functions import *

@pytest.mark.order(3)
class Test_author_page_features:
    def test_author_map_locations(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_from_api = api.authors.get_authors()
        authors_from_web = authors_page.get_author_container()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_from_web[-1]
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        homeLatitude, homeLongitude = author_page.get_home_location()
        assert round(last_author_from_api.homeLatitude, 4) == homeLatitude
        assert round(last_author_from_api.homeLongitude, 4) == homeLongitude

    def test_author_page_contant_of_books(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        authors_page = page.click_authors_button()
        authors_from_api = api.authors.get_authors()
        authors_from_web = authors_page.get_author_container()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_from_web[-1]
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        books_of_author_web = author_page.get_book_container()
        books_of_author_api = api.authors.get_authors_by_id(id=last_author_from_api.id).books
        assert len(books_of_author_web) == len(books_of_author_api)
        for i in range(len(books_of_author_web)):
            assert books_of_author_api[i]["name"] == author_page.get_book_name(books_of_author_web[i])
            assert str(books_of_author_api[i]["amountInStock"]) == author_page.get_ammount_in_stock_of_book(books_of_author_web[i])
            assert books_of_author_api[i]["imageUrl"] == author_page.get_book_img(books_of_author_web[i])
            assert str(books_of_author_api[i]["price"]) == author_page.get_book_price(books_of_author_web[i])
            assert books_of_author_api[i]["description"] == author_page.get_book_details(books_of_author_web[i])

    def test_author_page_contant_of_books_after_post(self, get_to_main_page, get_api_UnAutho,get_create_book_dto):
        page = get_to_main_page
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        authors_page = page.click_authors_button()
        authors_from_api = api.authors.get_authors()
        authors_from_web = authors_page.get_author_container()
        last_author_from_api = authors_from_api[-1]
        last_author_from_web = authors_from_web[-1]
        book = get_create_book_dto
        book.authorId = last_author_from_api.id
        res_post = api.books.post_books(data=book,id=book.authorId)
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        books_of_author_web = author_page.get_book_container()
        books_of_author_api = api.authors.get_authors_by_id(id=last_author_from_api.id).books
        assert len(books_of_author_web) == len(books_of_author_api)
        assert res_post.name == author_page.get_book_name(books_of_author_web[-1])
        assert str(res_post.amountInStock) == author_page.get_ammount_in_stock_of_book(books_of_author_web[-1])
        assert res_post.imageUrl == author_page.get_book_img(books_of_author_web[-1])
        assert str(res_post.price) == author_page.get_book_price(books_of_author_web[-1])
        assert res_post.description == author_page.get_book_details(books_of_author_web[-1])

    def test_author_page_contant_of_books_after_put(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        books_of_author_api = api.authors.get_authors_by_id(id=last_author_from_api.id).books
        last_book_of_author_from_api = books_of_author_api[-1]
        last_book_of_author_from_api["name"] = "danny"
        book_convert = convert_to_bookDto(last_book_of_author_from_api)
        api.books.put_books_by_id(data=book_convert,id=book_convert.id)
        page.page_refrash()
        authors_page = page.click_authors_button()
        authors_from_web = authors_page.get_author_container()
        last_author_from_web = authors_from_web[-1]
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        books_of_author_web = author_page.get_book_container()
        assert len(books_of_author_web) == len(books_of_author_api)
        assert last_book_of_author_from_api["name"] == author_page.get_book_name(books_of_author_web[-1])
        assert str(last_book_of_author_from_api["amountInStock"]) == author_page.get_ammount_in_stock_of_book(
            books_of_author_web[-1])
        assert last_book_of_author_from_api["imageUrl"] == author_page.get_book_img(books_of_author_web[-1])
        assert str(last_book_of_author_from_api["price"]) == author_page.get_book_price(books_of_author_web[-1])
        assert last_book_of_author_from_api["description"] == author_page.get_book_details(books_of_author_web[-1])

    def test_author_page_contant_of_books_after_delete(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        register = make_register_account(USER_Admin)
        user_login = make_login_account(register)
        api = make_sesion_autho(get_api_UnAutho, user_login)
        authors_from_api = api.authors.get_authors()
        last_author_from_api = authors_from_api[-1]
        books_of_author_api = api.authors.get_authors_by_id(id=last_author_from_api.id).books
        last_book_of_author_from_api = books_of_author_api[-1]
        authors_page = page.click_authors_button()
        authors_from_web = authors_page.get_author_container()
        last_author_from_web = authors_from_web[-1]
        author_page = authors_page.click_go_to_author_page(last_author_from_web)
        last_book_of_author_web_before_delete = author_page.get_book_container()[-1]
        api.books.delete_books_by_id(id=last_book_of_author_from_api["id"])
        page.page_refrash()
        books_after_delete = author_page.get_book_container()
        last_book_of_author_web_after_delete = books_after_delete[-1]
        assert last_book_of_author_web_before_delete != last_book_of_author_web_after_delete
        assert last_book_of_author_web_before_delete not in books_after_delete
        assert last_book_of_author_from_api not in api.books.get_books()
