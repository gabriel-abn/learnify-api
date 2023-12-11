from faker import Faker

from src.domain.entities import Enrollment, EnrollmentProps
from src.domain.entities.course import Course
from tests.fixtures.mocks import make_fake_course

faker = Faker()


def make_fake_enrollment(
    enrollment_id: str = faker.uuid4(),
    student_id: str = faker.uuid4(),
    course: Course = make_fake_course(),
    rating: int = faker.pyint(),
) -> Enrollment:
    enrollment_props: EnrollmentProps = {
        "enrollment_id": enrollment_id,
        "student_id": student_id,
        "course": course,
        "rating": rating,
    }

    return Enrollment(enrollment_props)
