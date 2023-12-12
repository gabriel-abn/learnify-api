from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Lesson


class GetLessonParams(TypedDict):
    course_id: str
    module_id: str
    lesson_id: str


class GetLessonResult(TypedDict):
    module_id: str
    lesson: Lesson


class GetLesson(UseCase[GetLessonParams, GetLessonResult]):
    @abstractmethod
    def execute(self, params: GetLessonParams) -> GetLessonResult:
        pass
