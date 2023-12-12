from abc import abstractmethod

from src.domain.common.use_case import UseCase
from src.domain.entities.course import Lesson


class GetAllLessons(UseCase[None, list[Lesson]]):
    @abstractmethod
    def execute(self, params: None) -> list[Lesson]:
        pass
