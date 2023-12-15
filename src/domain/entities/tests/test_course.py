import pytest

from src.domain.common.domain_error import DomainError
from tests.mocks import make_fake_course


class TestCourse:
    def test_create_with_basic_data(self):
        course = make_fake_course(
            name="Test Course",
            description="Test Description",
            category="Test Category",
            price=100.00,
            course_id="test-course-id",
            instructor_id="test-instructor-id",
        )

        assert course.props["name"] == "Test Course"
        assert course.props["description"] == "Test Description"
        assert course.props["category"] == "Test Category"
        assert course.props["price"] == 100.00
        assert course.props["course_id"] == "test-course-id"
        assert course.props["instructor_id"] == "test-instructor-id"

    def test_should_raise_if_invalid_price(self):
        with pytest.raises(DomainError) as excinfo:
            make_fake_course(price=-1)

        assert excinfo.value.message == "Invalid price"

    def test_should_be_able_to_add_a_new_lesson(self):
        course = make_fake_course(course_id="test-course-id")

        module = course.get_all_modules()[0]

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="test-lesson-id",
            title="Test Lesson",
            description="Test Description",
            content_type="video",
            content_url=["Test Video"],
        )

        assert len(course.modules[0].lessons) == 1
        assert course.modules[0].lessons[0].title == "Test Lesson"
        assert course.modules[0].lessons[0].description == "Test Description"

    def test_should_be_able_to_remove_a_lesson(self):
        course = make_fake_course()
        module = course.get_all_modules()[0]

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="test-lesson-id",
            title="Test Lesson",
            description="Test Description",
            content_type="video",
            content_url=["Test Video"],
        )

        assert len(course.modules[0].lessons) == 1

        course.remove_lesson(module.module_id, "test-lesson-id")

        assert len(course.modules[0].lessons) == 0

    def test_should_be_able_to_update_a_lesson(self):
        course = make_fake_course()
        module = course.get_all_modules()[0]

        course.add_lesson(
            module_id=module.module_id,
            lesson_id="test-lesson-id",
            title="Test Lesson",
            description="Test Description",
            content_type="video",
            content_url=["Test Video"],
        )

        assert len(course.modules[0].lessons) == 1

        course.update_lesson(
            module.module_id,
            "test-lesson-id",
            title="Updated Test Lesson",
            description="Updated Test Description",
            content_type="video",
            content_url=["Test Video"],
        )

        assert len(course.modules[0].lessons) == 1
        assert course.modules[0].lessons[0].title == "Updated Test Lesson"
        assert course.modules[0].lessons[0].description == "Updated Test Description"
