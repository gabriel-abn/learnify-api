from dataclasses import dataclass, field
from typing import TypedDict

from src.domain.common.domain_error import DomainError
from src.domain.common.entity import Entity, UniqueEntityID


@dataclass
class Lesson:
    lesson_id: str
    title: str
    description: str
    content_type: str = field(default="video")
    content_url: list[str] = field(default_factory=list)
    position: int = field(default=0)


@dataclass
class Module:
    module_id: str = field(init=False)
    title: str
    course_id: str
    lessons: list[Lesson] = field(init=False, default_factory=list)
    position: int = field(default=0)

    def __post_init__(self):
        self.module_id = f"{self.course_id}{UniqueEntityID.generate()}"
        self.lessons = []


class CourseProps(TypedDict):
    course_id: str
    name: str
    description: str
    category: str
    price: float
    instructor_id: str


class Course(Entity[CourseProps]):
    modules: list[Module]

    def __init__(self, props: CourseProps) -> None:
        if props["price"] < 0:
            raise DomainError("Invalid price")

        self.modules = [Module(title=props["name"], course_id=props["course_id"])]

        self.props = props

    def equals(self, object: Entity) -> bool:
        return super().equals(object)

    def init_modules(self) -> None:
        self.modules = []

    def add_module(self, title: str) -> None:
        module = Module(title=title, course_id=self.props["course_id"])

        self.modules.append(module)

    def get_module(self, module_id: str) -> Module:
        return next(module for module in self.modules if module.module_id == module_id)

    def get_all_modules(self) -> list[Module]:
        return self.modules

    def remove_module(self, module_id: str) -> None:
        self.modules = [
            module for module in self.modules if module.module_id != module_id
        ]

    def update_module(self, module_id: str, title: str) -> None:
        module = next(
            module for module in self.modules if module.module_id == module_id
        )

        module.title = title

    def add_lesson(
        self,
        module_id: str,
        lesson_id: str,
        title: str,
        description: str,
        content_type: str,
        content_url: list[str],
    ) -> None:
        for module in self.modules:
            if module.module_id == module_id:
                lesson = Lesson(
                    lesson_id=lesson_id,
                    title=title,
                    description=description,
                    content_type=content_type,
                    content_url=content_url,
                )

                module.lessons.append(lesson)
                break
        else:
            raise DomainError("Module not found")

    def remove_lesson(self, module_id: str, lesson_id: str) -> None:
        for module in self.modules:
            if module.module_id == module_id:
                module.lessons = [
                    lesson for lesson in module.lessons if lesson.lesson_id != lesson_id
                ]
                break
        else:
            raise DomainError("Module not found")

    def update_lesson(
        self,
        module_id: str,
        lesson_id: str,
        title: str,
        description: str,
        content_type: str,
        content_url: list[str],
    ) -> None:
        for module in self.modules:
            if module.module_id == module_id:
                for lesson in module.lessons:
                    if lesson.lesson_id == lesson_id:
                        lesson.title = title
                        lesson.description = description
                        lesson.content_type = content_type
                        lesson.content_url = content_url
                        break
                break
        else:
            raise DomainError("Module not found")

    def get_lesson(self, module_id: str, lesson_id: str) -> Lesson:
        for module in self.modules:
            if module.module_id == module_id:
                for lesson in module.lessons:
                    if lesson.lesson_id == lesson_id:
                        return lesson
        else:
            raise DomainError("Module not found")

    def get_all_lessons(self) -> list[Lesson]:
        lessons = []

        for module in self.modules:
            for lesson in module.lessons:
                lessons.append(lesson)

        return lessons
