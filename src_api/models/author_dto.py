from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj
from src_api.models.book_dto import BookDto


@dataclass
class AuthorDto(Base_Obj):
    id: str
    name: str
    homeLatitude: float
    homeLongitude: float
    books: list = True

    def __post_init__(self):
        if self.books is True:
            books = []
            for book in self.books:
                books.append(BookDto(**book))
            self.books = books

