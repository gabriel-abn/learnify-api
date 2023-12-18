from unittest.mock import Mock

import pytest

from src.application.common.application_error import ApplicationError
from src.application.repositories import ICourseRepository, ILessonRepository
from src.application.use_cases.management.course.lesson.create_lesson_use_case import (
    CreateLessonUseCase,
)
from src.domain.entities.course import Course
from src.domain.use_cases.management.course import CreateLesson
from src.domain.use_cases.management.course.lesson.create_lesson import (
    CreateLessonParams,
)
from tests.mocks import make_fake_course


class TestCreateLesson:
    sut: CreateLesson
    fake_course: Course
    fake_params: CreateLessonParams

    def setup_method(self):
        self.fake_course = make_fake_course()

        self.lesson_repo = Mock(spec=ILessonRepository)
        self.course_repo = Mock(spec=ICourseRepository)

        self.fake_params = {
            "course_id": self.fake_course.id,
            "module_id": self.fake_course.modules[0].module_id,
            "title": "any_name",
            "description": "any_description",
            "content_type": "video",
            "content_url": ["any_content_url"],
            "position": 0,
        }

        self.sut = CreateLessonUseCase(
            lesson_repository=self.lesson_repo, course_repository=self.course_repo
        )

    def test_should_call_repository_with_correct_params(self):
        self.course_repo.get.return_value = True, self.fake_course
        self.lesson_repo.save.return_value = True, "any_lesson"

        self.sut.execute(self.fake_params)

        self.course_repo.get.assert_called_once_with(self.fake_course.id)
        self.lesson_repo.save.assert_called_once()

    def test_repository_should_restore_course(self):
        self.course_repo.get.return_value = True, self.fake_course
        self.lesson_repo.save.return_value = True, "any_lesson"

        self.sut.execute(self.fake_params)

        self.course_repo.get.assert_called_once_with(self.fake_course.id)

    def test_should_create_lesson_id(self):
        self.course_repo.get.return_value = True, self.fake_course
        self.lesson_repo.save.return_value = True, "any_lesson"

        result = self.sut.execute(self.fake_params)

        assert result["lesson_id"] is not None

    def test_should_raise_exception_if_course_does_not_exist(self):
        self.course_repo.get.return_value = False, None

        pytest.raises(ApplicationError, self.sut.execute, self.fake_params).match(
            "Course not found."
        )
