from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class MakeEnrollmentParams(TypedDict):
    student_id: int
    course_id: int


class MakeEnrollmentResult(TypedDict):
    enrollment_id: int
    enrollment_date: str


class MakeEnrollment(UseCase[MakeEnrollmentParams, MakeEnrollmentResult]):
    @abstractmethod
    def execute(self, params: MakeEnrollmentParams) -> MakeEnrollmentResult:
        pass
