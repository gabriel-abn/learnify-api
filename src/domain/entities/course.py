from typing import TypedDict

from src.domain.common.entity import Entity


class CourseProps(TypedDict):
    course_id: str
    name: str
    description: str
    category: str
    price: float
    instructor_id: str


class Course(Entity[CourseProps]):
    lessons: list[str] = []

    def __init__(self, props: CourseProps) -> None:
        self.props = props

    def equals(self, object: Entity) -> bool:
        return super().equals(object)
