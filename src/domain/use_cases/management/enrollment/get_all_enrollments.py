from abc import abstractmethod

from src.domain.common.use_case import UseCase
from src.domain.entities.enrollment import Enrollment


class GetAllEnrollments(UseCase[None, list[Enrollment]]):
    @abstractmethod
    def execute(self, params: None) -> list[Enrollment]:
        pass
