from abc import abstractmethod
from typing import Required, TypedDict

from src.domain.common.use_case import UseCase


class EditLessonParams(TypedDict, total=False):
    lesson_id: Required[str]
    name: str
    description: str
    content_type: str
    content_url: str
    position: int


class EditLessonResult(TypedDict):
    lesson_id: str
    updated: bool


class EditLesson(UseCase[EditLessonParams, EditLessonResult]):
    @abstractmethod
    def execute(self, params: EditLessonParams) -> EditLessonResult:
        pass
