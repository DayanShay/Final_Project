from dataclasses import dataclass
from src_api.models import *
from src_api.models.base_obj import Base_Obj


@dataclass
class Author(Base_Obj):
    id: int
    homeLatitude: float
    homeLongitude: float
    name: str = True
    books: list = True

    def __post_init__(self):
        if self.books is True:
            books = []
            for book in self.books:
                books.append(Book(**book))
            self.books = books
