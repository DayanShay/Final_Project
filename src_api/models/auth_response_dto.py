from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class AuthResponseDto(Base_Obj):
    userId: str = True
    token: str = True
    refreshToken: str = True
