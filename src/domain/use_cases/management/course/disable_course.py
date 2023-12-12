from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class DisableCourseParams(TypedDict):
    course_id: str


class DisableCourseResult(TypedDict):
    disabled: bool
    updated_at: str


class DisableCourse(UseCase[DisableCourseParams, DisableCourseResult]):
    @abstractmethod
    def execute(self, params: DisableCourseParams) -> DisableCourseResult:
        pass
