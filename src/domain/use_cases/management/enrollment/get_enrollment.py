from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class GetEnrollmentParams(TypedDict):
    enrollment_id: int


class GetEnrollmentResult(TypedDict):
    enrollment_id: int
    enrollment_date: str
    is_cancelled: bool


class GetEnrollment(UseCase[GetEnrollmentParams, GetEnrollmentResult]):
    @abstractmethod
    def execute(self, params: GetEnrollmentParams) -> GetEnrollmentResult:
        pass
