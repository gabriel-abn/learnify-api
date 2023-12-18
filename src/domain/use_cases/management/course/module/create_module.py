from abc import abstractmethod
from typing import Optional, TypedDict

from src.domain.common.use_case import UseCase


class CreateModuleParams(TypedDict):
    course_id: str
    title: str
    position: Optional[int]


class CreateModuleResult(TypedDict):
    module_id: str
    course_id: str
    position: int


class CreateModule(UseCase[CreateModuleParams, CreateModuleResult]):
    @abstractmethod
    def execute(self, params: CreateModuleParams) -> CreateModuleResult:
        pass
