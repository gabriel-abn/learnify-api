from dataclasses import dataclass
from typing import TypedDict

from src.domain.common import DomainError, Entity, UniqueEntityID
from src.domain.entities import Course


class EnrollmentProps(TypedDict):
    enrollment_id: str
    student_id: str
    course: Course
    enrollment_date: str
    rating: float


class Enrollment(Entity[EnrollmentProps]):
    completed_lessons: list[str]
    completition_status: float

    def __init__(self, props: EnrollmentProps) -> None:
        if not props:
            raise DomainError("Enrollment must have props")

        self._id = UniqueEntityID(props["enrollment_id"])
        self.props = props

        self.completed_lessons = []
        self.completition_status = 0

    def equals(self, object: Entity) -> bool:
        return isinstance(object, Enrollment) and object.id == self.id

    def complete_lesson(self, lesson_id: str) -> None:
        self.completed_lessons.append(lesson_id)

        self.completition_status = round(
            len(self.completed_lessons) / len(self.props["course"].get_all_lessons()), 2
        )

    def get_progress_report(self):
        return ProgressReport(
            course_id=self.props["course"].props["course_id"],
            completition_status=self.completition_status,
            completed_lessons=self.completed_lessons,
        )


@dataclass
class ProgressReport:
    course_id: str
    completition_status: float
    completed_lessons: list[str]
