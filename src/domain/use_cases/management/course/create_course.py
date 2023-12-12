from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class CreateCourseParams(TypedDict):
    name: str
    description: str
    category: str
    price: float


class CreateCourseResult(TypedDict):
    id: str


class CreateCourse(UseCase[CreateCourseParams, CreateCourseResult]):
    @abstractmethod
    def execute(self, params: CreateCourseParams) -> CreateCourseResult:
        pass
