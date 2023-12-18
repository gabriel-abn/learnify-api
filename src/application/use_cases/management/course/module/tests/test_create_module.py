from unittest.mock import Mock

import pytest

from src.application.common import ApplicationError
from src.application.repositories import ICourseRepository, IModuleRepository
from src.application.use_cases.management.course.module.create_module_use_case import (
    CreateModuleUseCase,
)
from src.domain.use_cases.management.course.module.create_module import (
    CreateModule,
    CreateModuleParams,
)
from tests.mocks import make_fake_course, make_fake_module


class TestCreateModule:
    sut: CreateModule
    fake_params: CreateModuleParams

    def setup_method(self):
        self.module_repository = Mock(spec=IModuleRepository)
        self.course_repository = Mock(spec=ICourseRepository)

        self.sut = CreateModuleUseCase(
            course_repository=self.course_repository,
            module_repository=self.module_repository,
        )

        self.fake_course = make_fake_course()
        self.fake_module = make_fake_module(course_id=self.fake_course.id)

        self.fake_params = {
            "course_id": self.fake_course.id,
            "title": "any_title",
            "position": 0,
        }

    def test_should_raise_if_course_not_found(self):
        self.course_repository.get.return_value = False, None

        pytest.raises(ApplicationError, self.sut.execute, self.fake_params).match(
            "Course not found."
        )

    def test_should_call_get_course_with_correct_params(self):
        self.course_repository.get.return_value = True, self.fake_course
        self.module_repository.create.return_value = True, self.fake_module.module_id

        self.sut.execute(self.fake_params)

        self.course_repository.get.assert_called_once_with(
            self.fake_params["course_id"]
        )

    def test_should_call_create_module_repo_method(self):
        self.course_repository.get.return_value = True, self.fake_course
        self.module_repository.create.return_value = True, self.fake_module.module_id

        self.sut.execute(self.fake_params)

        self.module_repository.create.assert_called_once()

    def test_should_return_module_id_if_success(self):
        self.course_repository.get.return_value = True, self.fake_course
        self.module_repository.create.return_value = True, self.fake_module.module_id

        result = self.sut.execute(self.fake_params)

        assert result["module_id"] == self.fake_module.module_id
        assert result["course_id"] == self.fake_module.course_id
