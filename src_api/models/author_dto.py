from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj
from src_api.models.book import Book


@dataclass
class AuthorDto(Base_Obj):
    id: str
    name: str
    homeLatitude: float
    homeLongitude: float
    books : list = True

    def __post_init__(self):
        books = []
        for book in self.books:
            books.append(Book(**book))
        self.books = books

