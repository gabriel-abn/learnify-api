from dataclasses import dataclass, field
from datetime import datetime
from typing import TypedDict

from src.domain.common import DomainError, Entity, UniqueEntityID
from src.domain.entities import Course


class EnrollmentProps(TypedDict):
    enrollment_id: str
    student_id: str
    course: Course
    rating: float


@dataclass
class ProgressReport:
    course_id: str
    completition_status: float
    completed_lessons: list[str]

    def __str__(self) -> str:
        return f"Course: {self.course_id} \nStatus: {self.completition_status} \nCompleted lessons: {self.completed_lessons}"


@dataclass
class ConclusionCertificate:
    certificate_id: str
    course_id: str
    student_id: str
    completion_date: str = field(
        init=False, default=datetime.now().strftime("%Y-%m-%d")
    )


class Enrollment(Entity[EnrollmentProps]):
    completed_lessons: list[str]
    completition_status: float
    enrollment_date: str

    def __init__(self, props: EnrollmentProps) -> None:
        if not props:
            raise DomainError("Enrollment must have props")

        if props["enrollment_id"] == "":
            raise DomainError("Enrollment must have base ID")

        if props["student_id"] == "":
            raise DomainError("Enrollment must have Student ID")

        self._id = UniqueEntityID(props["enrollment_id"])
        self.props = props

        self.completed_lessons = []
        self.completition_status = 0
        self.enrollment_date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def equals(self, object: Entity) -> bool:
        return isinstance(object, Enrollment) and object.id == self.id

    def complete_lesson(self, lesson_id: str) -> None:
        self.completed_lessons.append(lesson_id)

        self.completition_status = round(
            len(self.completed_lessons) / len(self.props["course"].get_all_lessons()), 2
        )

    def get_progress_report(self) -> ProgressReport:
        return ProgressReport(
            course_id=self.props["course"].props["course_id"],
            completition_status=self.completition_status,
            completed_lessons=self.completed_lessons,
        )

    def generate_certificate(self) -> ConclusionCertificate:
        all_lessons = sorted(
            [lesson.lesson_id for lesson in self.props["course"].get_all_lessons()]
        )

        if sorted(self.completed_lessons) == all_lessons:
            return ConclusionCertificate(
                certificate_id=self.props["enrollment_id"],
                course_id=self.props["course"].props["course_id"],
                student_id=self.props["student_id"],
            )

        raise DomainError("Student must complete all lessons to generate certificate.")
