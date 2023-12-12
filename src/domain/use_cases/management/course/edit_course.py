from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class EditCourseParams(TypedDict):
    course_id: str
    name: str
    description: str
    category: str
    price: float


class EditCourse(UseCase[EditCourseParams, bool]):
    @abstractmethod
    def execute(self, params: EditCourseParams) -> bool:
        pass
