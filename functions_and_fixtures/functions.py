from src_api.models import *


def convert_to_bookDto(book):
    amountInStock = book.amountInStock
    authorId = book.authorId
    description = book.description
    id = book.id
    imageUrl = book.imageUrl
    name = book.name
    price = book.price
    return BookDto(id=id,
                   amountInStock=amountInStock,
                   authorId=authorId,
                   description=description,
                   imageUrl=imageUrl,
                   name=name,
                   price=price)


def make_login_account(user: ApiUserDto):
    login_user = LoginDto(user.email, user.password)
    return login_user


def make_register_account(info: dict):
    reguster_user = ApiUserDto(**info)
    return reguster_user


def make_dup_user_msg(email):
    dup_msg = '{"DuplicateUserName":' + f'["Username \'{email}\' is already taken."]'"}"
    return dup_msg


def make_sesion_autho(api, user_login):
    res = api.account.post_login(data=user_login)
    my_token = res.token if not isinstance(res, dict) else ""
    HEADERS = {'Authorization': f'Bearer {my_token}'}
    api.update_session_header(HEADERS)
    return api


def make_sesion_Unautho(api):
    HEADERS = {'Authorization': ''}
    api.update_session_header(HEADERS)
    return api


def make_purches_msg(book_name):
    return f'Thank you for your purchase of {book_name}'


def delete_all_authors_and_books_created(api_from_test):
    api = api_from_test
    authors = api.authors.get_authors()
    for author in authors:
        if author.id > 3:
            api.authors.delete_authors_by_id(id=str(author.id))
    books = api.books.get_books()
    for book in books:
        if book.id > 6:
            api.books.delete_books_by_id(id=str(book.id))
