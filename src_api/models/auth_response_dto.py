from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class AuthResponseDto(Base_Obj):
    userId : str
    token : str
    refreshToken : str

    def __post_init__(self):
        pass