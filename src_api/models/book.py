from dataclasses import dataclass
from src_api.models.author import Author
from src_api.models.base_obj import Base_Obj


@dataclass
class Book(Base_Obj):
    id: str
    name: str
    description: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int
    author: Author = None

    def __post_init__(self):
        if self.author is not None:
            author = Author(*self.author)
        self.author = author

