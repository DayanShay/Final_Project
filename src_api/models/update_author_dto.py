from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class UpdateAuthorDto(Base_Obj):
    name: str
    homeLatitude: float
    homeLongitude: float
    id: int

    def __post_init__(self):
        pass
