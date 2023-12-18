from abc import ABC, abstractmethod

from src.domain.entities.course import Course


class ICourseRepository(ABC):
    @abstractmethod
    def get(self, course_id: str) -> tuple[bool, Course]:
        pass

    @abstractmethod
    def save(self, course: Course) -> tuple[bool, str]:
        pass
