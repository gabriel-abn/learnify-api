from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Lesson


class GetLessonsFromModuleParams(TypedDict):
    course_id: str
    module_id: str


class GetLessonsFromModuleResult(TypedDict):
    lessons: list[Lesson]


class GetLessonsFromModule(
    UseCase[GetLessonsFromModuleParams, GetLessonsFromModuleResult]
):
    @abstractmethod
    def execute(self, params: GetLessonsFromModuleParams) -> GetLessonsFromModuleResult:
        pass
