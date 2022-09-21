from dataclasses import dataclass
from src_api.obj_models.author import Author
from src_api.obj_models.base_obj import Base_Obj


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



