from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class Author(Base_Obj):
    id : str
    name : str
    homeLatitude: float
    homeLongitude :float
    books : list

    def __post_init__(self):
        pass