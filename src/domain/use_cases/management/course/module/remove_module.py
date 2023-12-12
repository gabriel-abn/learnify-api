from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class RemoveModuleParams(TypedDict):
    course_id: str
    module_id: str


class RemoveModuleResult(TypedDict):
    removed: bool


class RemoveModule(UseCase[RemoveModuleParams, RemoveModuleResult]):
    @abstractmethod
    def execute(self, params: RemoveModuleParams) -> RemoveModuleResult:
        pass
