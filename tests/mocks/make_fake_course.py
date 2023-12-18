from faker import Faker
from faker.providers import person

from src.domain.entities import Course, CourseProps
from src.domain.entities.course import Lesson, Module

faker = Faker()
faker.add_provider(person)


def make_fake_course(
    course_id: str = faker.uuid4(),
    name: str = faker.first_name(),
    description: str = faker.text(),
    category: str = faker.word(),
    price: float = faker.pyint(),
    instructor_id: str = faker.uuid4(),
) -> Course:
    course_props: CourseProps = {
        "course_id": course_id,
        "name": name,
        "description": description,
        "category": category,
        "price": price,
        "instructor_id": instructor_id,
    }

    course = Course(course_props)

    return course


def make_fake_module(
    course_id: str = faker.uuid4(),
    title: str = faker.first_name(),
):
    return Module(
        course_id=course_id,
        title=title,
    )


def make_fake_lesson(
    lesson_id: str = faker.uuid4(),
    title: str = faker.first_name(),
    description: str = faker.text(),
    content_type: str = "video",
    content_url: list[str] = [faker.url()],
    position: int = 0,
):
    return Lesson(
        lesson_id=lesson_id,
        title=title,
        description=description,
        content_type=content_type,
        content_url=content_url,
        position=position,
    )
