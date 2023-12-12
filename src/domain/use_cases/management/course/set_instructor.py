from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class SetInstructorParams(TypedDict):
    course_id: str
    instructor_id: str


class SetInstructorResult(TypedDict):
    user_id: str


class SetInstructor(UseCase[SetInstructorParams, SetInstructorResult]):
    @abstractmethod
    def execute(self, params: SetInstructorParams) -> SetInstructorResult:
        pass
