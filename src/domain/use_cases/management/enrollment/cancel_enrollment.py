from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class CancelEnrollmentParams(TypedDict):
    enrollment_id: int


class CancelEnrollmentResult(TypedDict):
    enrollment_date: str
    is_cancelled: bool


class CancelEnrollment(UseCase[CancelEnrollmentParams, CancelEnrollmentResult]):
    @abstractmethod
    def execute(self, params: CancelEnrollmentParams) -> CancelEnrollmentResult:
        pass
