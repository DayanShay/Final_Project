from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class ApiUserDto(Base_Obj):
    email: str
    password: str
    firstName: str
    lastName: str

    def __post_init__(self):
        pass
