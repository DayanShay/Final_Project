from dataclasses import dataclass
from src_api.models.author import Author
from src_api.models.base_obj import Base_Obj


@dataclass
class BookDto(Base_Obj):
    id: str
    name: str
    description: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int
    author: Author

    def __post_init__(self):
        pass
