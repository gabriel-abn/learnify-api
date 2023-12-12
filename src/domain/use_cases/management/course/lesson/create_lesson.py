from abc import abstractmethod
from typing import Optional, TypedDict

from src.domain.common.use_case import UseCase


class CreateLessonParams(TypedDict):
    course_id: str
    module_id: str
    title: str
    description: str
    content_type: Optional[str]
    content_url: Optional[list[str]]
    position: Optional[int]


class CreateLessonResult(TypedDict):
    lesson_id: str


class CreateLesson(UseCase[CreateLessonParams, CreateLessonResult]):
    @abstractmethod
    def execute(self, params: CreateLessonParams) -> CreateLessonResult:
        pass
