from typing import TypedDict

from src.domain.common import DomainError, Entity
from src.domain.entities import Enrollment

ROLES = ["ADMIN", "STUDENT", "INSTRUCTOR"]


class UserProps(TypedDict):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    role: str


class User(Entity[UserProps]):
    enrollments: list[Enrollment]

    def __init__(self, props: UserProps) -> None:
        if not props:
            raise DomainError("User must have props")

        if props["role"].upper() not in ROLES:
            raise DomainError("User must have a valid role")

        props["role"] = props["role"].upper()

        self.__validate_password(props["password"])

        if not props["first_name"].isalpha():
            raise DomainError("Invalid first name")

        if not props["last_name"].isalpha():
            raise DomainError("Invalid last name")

        super().__init__(props)
        self.enrollments = []

    def equals(self, object: Entity) -> bool:
        return isinstance(object, User) and object.id == self.id

    def make_enrollment(self, enrollment: Enrollment) -> None:
        self.enrollments.append(enrollment)

    def complete_lesson(self, enrollment_id: str, lesson_id: str) -> None:
        for enrollment in self.enrollments:
            if enrollment.id == enrollment_id:
                enrollment.complete_lesson(lesson_id)
                break
        else:
            raise DomainError("User is not enrolled in this course")

    def get_progress_report(self, course_id: str):
        for enrollment in self.enrollments:
            if enrollment.props["course"].props["course_id"] == course_id:
                return enrollment.get_progress_report()
        else:
            raise DomainError("User is not enrolled in this course")

    def __validate_password(self, password: str) -> None:
        if not any(char.isupper() for char in password):
            raise DomainError("Password must have a upper case letter")

        if not any(char.islower() for char in password):
            raise DomainError("Password must have a lower case letter")

        if not any(char.isdigit() for char in password):
            raise DomainError("Password must have a number")

        if not any(char in "!@#$%^&*()-+?_=,<>/;:[]{}" for char in password):
            raise DomainError("Password must have a special character")

        if len(password) < 8:
            raise DomainError("Password must have at least 8 characters")
