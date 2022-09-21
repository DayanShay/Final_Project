from dataclasses import dataclass
from src_api.obj_models.base_obj import Base_Obj


@dataclass
class CreateBookDto(Base_Obj):
    name: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int
    description: str = True


