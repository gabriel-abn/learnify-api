from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class RemoveCourseParams(TypedDict):
    course_id: str


class RemoveCourse(UseCase[RemoveCourseParams, bool]):
    @abstractmethod
    def execute(self, params: RemoveCourseParams) -> bool:
        pass
