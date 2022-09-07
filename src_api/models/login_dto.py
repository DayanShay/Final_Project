from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class LoginDto(Base_Obj):
    email: str
    password: str

    def __post_init__(self):
        pass