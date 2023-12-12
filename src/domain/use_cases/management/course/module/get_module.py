from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Module


class GetModuleParams(TypedDict):
    course_id: str
    module_id: str


class GetModule(UseCase[GetModuleParams, Module]):
    @abstractmethod
    def execute(self, params: GetModuleParams) -> Module:
        pass
