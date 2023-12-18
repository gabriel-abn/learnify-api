from abc import ABC, abstractmethod

from src.domain.entities.course import Lesson


class ILessonRepository(ABC):
    @abstractmethod
    def save(self, lesson: Lesson) -> tuple[bool, str]:
        pass

    @abstractmethod
    def get(self, lesson_id: str) -> tuple[bool, Lesson]:
        pass

    @abstractmethod
    def get_all(self, course_id: str) -> tuple[bool, list[Lesson]]:
        pass
