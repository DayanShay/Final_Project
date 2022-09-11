from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class CreateBookDto(Base_Obj):
    name: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int > 1 < 2147486347
    description: str = True

    def __post_init__(self):
        pass
