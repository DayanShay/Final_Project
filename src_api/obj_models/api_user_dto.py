from dataclasses import dataclass
from src_api.obj_models.base_obj import Base_Obj


@dataclass
class ApiUserDto(Base_Obj):
    email: str
    password: str
    firstName: str
    lastName: str

