from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Course


class GetCourseParams(TypedDict):
    course_id: str


class GetCourse(UseCase[GetCourseParams, Course]):
    @abstractmethod
    def execute(self, params: GetCourseParams) -> Course:
        pass
