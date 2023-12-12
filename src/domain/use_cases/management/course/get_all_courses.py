from abc import abstractmethod

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Course


class GetAllCourses(UseCase[None, list[Course]]):
    @abstractmethod
    def execute(self, params: None) -> list[Course]:
        pass
