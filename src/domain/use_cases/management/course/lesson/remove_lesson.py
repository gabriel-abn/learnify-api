from abc import abstractmethod
from typing import TypedDict

from src.domain.common import UseCase


class RemoveLessonParams(TypedDict):
    course_id: str
    module_id: str
    lesson_id: str


class RemoveLessonResult(TypedDict):
    removed: bool


class RemoveLesson(UseCase[RemoveLessonParams, RemoveLessonResult]):
    @abstractmethod
    def execute(self, params: RemoveLessonParams) -> RemoveLessonResult:
        pass
