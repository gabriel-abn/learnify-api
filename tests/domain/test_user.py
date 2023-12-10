import pytest

from src.domain.common import DomainError
from src.domain.entities import User
from tests.fixtures.mocks import make_fake_course, make_fake_enrollment, make_fake_user


class TestUser:
    @pytest.mark.parametrize(
        "password, error_message",
        [
            ("abc123", "Password must have a upper case letter"),
            ("ABC123", "Password must have a lower case letter"),
            ("ABCabc", "Password must have a number"),
            ("ABCabc1", "Password must have a special character"),
            ("ABab1!", "Password must have at least 8 characters"),
        ],
    )
    def test_must_have_valid_password(self, password: str, error_message: str):
        """
        Scenario: A user tries to register with a password that does not meet the
        minimum length or complexity requirements.

        Expected behavior: The registration process should fail for the user,
        with an error message specifying the password requirements.
        """
        props = make_fake_user(password=password)

        assert pytest.raises(DomainError, User, props).match(error_message)

    @pytest.mark.parametrize(
        "field, name, error",
        [
            ("first_name", "", "Invalid first name"),
            ("last_name", "", "Invalid last name"),
        ],
    )
    def test_must_have_valid_name(self, field: str, name: str, error: str):
        """
        Scenario: A user tries to register with an empty first name or last name,
        or with a name containing special characters or numbers.

        Expected behavior: The registration process should fail for the user,
        with an errormessage stating the required format for names.
        """
        user_props = make_fake_user(**{field: name})

        assert pytest.raises(DomainError, User, user_props).match(error)

    def test_can_be_enrolled_in_multiple_courses(self):
        """
        Scenario: A user enrolls in several courses offered on the platform.

        Expected behavior: The user's enrollment data should be stored correctly,
        and they should have access to the enrolled courses.
        """
        user = User(make_fake_user(role="STUDENT"))

        for i in range(5):
            enrollment = make_fake_enrollment(enrollment_id=f"enrollment_id_{i}")
            user.make_enrollment(enrollment)

        assert user.enrollments is not None
        assert len(user.enrollments) == 5

    def test_user_can_complete_lessons_and_modules(self):
        """
        Scenario: A user completes lessons and modules within a course.

        Expected behavior: The user's progress should be tracked and stored correctly,
        reflecting their completed lessons and modules.
        """
        course = make_fake_course(course_id="course_id_1")
        course.add_module("Module 1")
        course.add_lesson(
            module_id=course.modules[0].module_id,
            lesson_id="test-lesson-id",
            title="Test Lesson",
            description="Test Description",
            content_type="video",
            content_url=["Test Video"],
        )

        user = User(make_fake_user(role="STUDENT"))

        enrollment = make_fake_enrollment(
            enrollment_id="enrollment_id_1", course=course
        )

        user.make_enrollment(enrollment)
        user.complete_lesson("enrollment_id_1", "lesson_id_1")

        assert user.enrollments[0].completed_lessons is not None
        assert user.enrollments[0].completition_status > 0

    def test_user_can_access_their_progress_report(self):
        """
        Scenario: A user wants to see their progress in a course.

        Expected behavior: The user should be able to access a progress report
        that shows their progress in the course.
        """
        course = make_fake_course(course_id="course_id_1")

        course.add_module("Module 1")

        course.add_lesson(
            module_id=course.modules[0].module_id,
            lesson_id="test-lesson-id",
            title="Test Lesson",
            description="Test Description",
            content_type="video",
            content_url=["Test Video"],
        )

        user = User(make_fake_user(role="STUDENT"))

        enrollment = make_fake_enrollment(
            enrollment_id="enrollment_id_1",
            course=course,
        )

        user.make_enrollment(enrollment)

        user.complete_lesson("enrollment_id_1", "lesson_id_1")
        progress_report = user.get_progress_report("course_id_1")

        assert user.enrollments[0].completed_lessons is not None

        assert progress_report is not None
        assert progress_report.course_id == "course_id_1"
        assert progress_report.completition_status > 0
