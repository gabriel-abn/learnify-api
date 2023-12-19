from unittest.mock import Mock

import pytest

from src.application.common.application_error import ApplicationError
from src.application.repositories.course_repository import ICourseRepository
from src.application.use_cases.management.course.create_course_use_case import (
    CreateCourseUseCase,
)
from src.domain.use_cases.management.course.create_course import (
    CreateCourse,
    CreateCourseParams,
)
from tests.mocks.make_fake_course import make_fake_course


class TestCreateCourse:
    sut: CreateCourse
    fake_params: CreateCourseParams

    def setup_method(self):
        self.repository = Mock(spec=ICourseRepository)

        self.sut = CreateCourseUseCase(course_repository=self.repository)

        self.fake_params = {
            "name": "any_name",
            "description": "any_description",
            "category": "any_category",
            "price": 100,
        }

    def test_should_call_repository_with_correct_params(self):
        fake_course = make_fake_course()
        self.repository.save.return_value = True, fake_course

        self.sut.execute(self.fake_params)

        self.repository.save.assert_called_once()

    def test_should_return_correct_result(self):
        fake_course = make_fake_course()
        self.repository.save.return_value = True, fake_course

        response = self.sut.execute(self.fake_params)

        assert response["id"] is not None

    def test_should_raise_if_repository_raises(self):
        self.repository.save.return_value = False, None

        pytest.raises(ApplicationError, self.sut.execute, self.fake_params).match(
            "Could not create course."
        )
