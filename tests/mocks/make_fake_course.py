from faker import Faker
from faker.providers import person

from src.domain.entities import Course, CourseProps

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
