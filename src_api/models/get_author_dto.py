from dataclasses import dataclass
from src_api.models.base_obj import Base_Obj


@dataclass
class GetAuthorDto(Base_Obj):
    id: str
    name: str
    homeLatitude: float
    homeLongitude: float

    def __post_init__(self):
        pass


