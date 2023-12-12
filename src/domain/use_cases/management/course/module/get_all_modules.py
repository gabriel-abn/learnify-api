from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Module


class GetAllModulesParams(TypedDict):
    course_id: str


class GetAllModules(UseCase[GetAllModulesParams, list[Module]]):
    @abstractmethod
    def execute(self, params: GetAllModulesParams) -> list[Module]:
        pass
