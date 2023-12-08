from typing import Optional

from src.domain.entities import Enrollment, EnrollmentProps


def make_fake_enrollment(props: Optional[EnrollmentProps]) -> Enrollment:
    enrollment_props: EnrollmentProps = {
        "enrollment_id": "any_id",
        "student_id": "any_id",
        "course_id": "any_id",
        "enrollment_date": "any_date",
        "rating": 0,
    }

    if props:
        enrollment_props.update(props)

    return Enrollment(enrollment_props)
