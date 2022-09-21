from dataclasses import dataclass
from src_api.obj_models.base_obj import Base_Obj


@dataclass
class ProblemDetails(Base_Obj):
    type: str = True
    title: str = True
    status: int = True
    detail: str = True
    instance: str = True
    traceId: str = True
    errors: str = True
    DuplicateUserName: str = True
