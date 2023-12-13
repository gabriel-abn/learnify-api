from datetime import datetime

from pytest import raises

from src.domain.common.domain_error import DomainError
from tests.fixtures.mocks.make_fake_course import make_fake_course
from tests.fixtures.mocks.make_fake_enrollment import make_fake_enrollment


class TestEnrollment:
    def test_should_create_enrollment(self):
        enrollment = make_fake_enrollment()

        assert enrollment is not None

        props = enrollment.get_props()

        assert all(prop is not None for prop in props.values())

    def test_should_not_create_enrollment_with_empty_props(self):
        with raises(DomainError) as exc:
            make_fake_enrollment(student_id="")

        assert exc.value.message == "Enrollment must have Student ID"

        with raises(DomainError) as exc:
            make_fake_enrollment(enrollment_id="")

        assert exc.value.message == "Enrollment must have base ID"

    def test_should_assing_enrollment_date(self):
        enrollment = make_fake_enrollment()

        assert enrollment.enrollment_date is not None
        assert enrollment.enrollment_date.strftime(
            "%Y-%m-%d"
        ) == datetime.now().strftime("%Y-%m-%d")

    def test_should_have_a_valid_course(self):
        enrollment = make_fake_enrollment()

        assert enrollment.props["course"] is not None
        assert enrollment.props["course"].props["course_id"] is not None

    def test_should_track_student_progress(self):
        course = make_fake_course()
        module = course.modules[0]

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_1",
            title="Lesson 1",
            description="Lesson 1",
            content_type="video",
            content_url=["random_url"],
        )

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_2",
            title="Lesson 2",
            description="Lesson 2",
            content_type="video",
            content_url=["random_url"],
        )

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_3",
            title="Lesson 3",
            description="Lesson 3",
            content_type="video",
            content_url=["random_url"],
        )

        enrollment = make_fake_enrollment(course=course)

        assert enrollment.props["course"] is not None
        assert enrollment.props["course"].props["course_id"] is not None

        enrollment.complete_lesson("lesson_1")
        enrollment.complete_lesson("lesson_2")

        assert enrollment.completition_status == 0.67
        assert len(enrollment.completed_lessons) == 2

    def test_should_generate_certificate(self):
        course = make_fake_course()
        module = course.modules[0]

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_1",
            title="Lesson 1",
            description="Lesson 1",
            content_type="video",
            content_url=["random_url"],
        )

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_2",
            title="Lesson 2",
            description="Lesson 2",
            content_type="video",
            content_url=["random_url"],
        )

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_3",
            title="Lesson 3",
            description="Lesson 3",
            content_type="video",
            content_url=["random_url"],
        )

        enrollment = make_fake_enrollment(course=course)

        assert enrollment.props["course"] is not None
        assert enrollment.props["course"].props["course_id"] is not None

        enrollment.complete_lesson("lesson_1")
        enrollment.complete_lesson("lesson_2")
        enrollment.complete_lesson("lesson_3")

        assert enrollment.completition_status == 1
        assert len(enrollment.completed_lessons) == 3

        certificate = enrollment.generate_certificate()

        assert certificate is not None
        assert certificate.certificate_id is not None
        assert certificate.course_id == course.props["course_id"]
        assert certificate.student_id == enrollment.props["student_id"]
        assert certificate.completion_date == datetime.now().strftime("%Y-%m-%d")

    def test_should_not_generate_certificate_if_course_is_not_completed(self):
        course = make_fake_course()
        module = course.modules[0]

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_1",
            title="Lesson 1",
            description="Lesson 1",
            content_type="video",
            content_url=["random_url"],
        )

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_2",
            title="Lesson 2",
            description="Lesson 2",
            content_type="video",
            content_url=["random_url"],
        )

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="lesson_3",
            title="Lesson 3",
            description="Lesson 3",
            content_type="video",
            content_url=["random_url"],
        )

        enrollment = make_fake_enrollment(course=course)

        enrollment.complete_lesson("lesson_1")
        enrollment.complete_lesson("lesson_2")

        with raises(DomainError) as exc:
            enrollment.generate_certificate()
            exc.match("Student must complete all lessons to generate certificate.")
