from unittest.mock import Mock

import pytest

from src.application.common import ApplicationError
from src.application.use_cases.management.account.register_user_use_case import (
    RegisterUserRepository,
    RegisterUserUseCase,
)
from src.domain.common.domain_error import DomainError
from src.domain.entities.user import User
from src.domain.use_cases.management.account import RegisterUser
from tests.fixtures.mocks.make_fake_user import make_fake_user


class TestRegisterUser:
    sut: RegisterUser

    def setup_method(self):
        self.repo = Mock(spec=RegisterUserRepository)
        self.repo.check_email_exists.return_value = False
        self.repo.check_username_exists.return_value = False
        self.sut = RegisterUserUseCase(repository=self.repo)

    def teardown_method(self):
        self.repo.reset_mock()

    def test_should_call_repository_with_correct_values(self):
        user_props = make_fake_user()

        self.repo.create.return_value = True

        result = self.sut.execute(
            {
                "email": user_props["email"],
                "first_name": user_props["first_name"],
                "last_name": user_props["last_name"],
                "password": user_props["password"],
                "role": user_props["role"],
                "username": user_props["username"],
            }
        )

        assert result["id"] is not None

        self.repo.create.assert_called_once()

    def test_should_raise_if_email_exists(self):
        user_props = make_fake_user()
        self.repo.create.return_value = User(user_props)

        self.sut.execute(
            {
                "email": user_props["email"],
                "first_name": user_props["first_name"],
                "last_name": user_props["last_name"],
                "password": user_props["password"],
                "role": user_props["role"],
                "username": user_props["username"],
            }
        )

        self.repo.check_email_exists.return_value = True

        with pytest.raises(ApplicationError, match="Email already exists."):
            self.sut.execute(
                {
                    "email": user_props["email"],
                    "first_name": user_props["first_name"],
                    "last_name": user_props["last_name"],
                    "password": user_props["password"],
                    "role": user_props["role"],
                    "username": user_props["username"],
                }
            )

    def test_should_raise_if_username_exists(self):
        user_props = make_fake_user()
        self.repo.create.return_value = User(user_props)

        self.sut.execute(
            {
                "email": user_props["email"],
                "first_name": user_props["first_name"],
                "last_name": user_props["last_name"],
                "password": user_props["password"],
                "role": user_props["role"],
                "username": user_props["username"],
            }
        )

        self.repo.check_username_exists.return_value = True

        with pytest.raises(ApplicationError, match="Username already exists."):
            self.sut.execute(
                {
                    "email": "another_email",
                    "first_name": user_props["first_name"],
                    "last_name": user_props["last_name"],
                    "password": user_props["password"],
                    "role": user_props["role"],
                    "username": user_props["username"],
                }
            )

    def test_should_raise_if_role_is_invalid(self):
        user_props = make_fake_user(role="invalid_role")

        with pytest.raises(DomainError):
            self.sut.execute(
                {
                    "email": user_props["email"],
                    "first_name": user_props["first_name"],
                    "last_name": user_props["last_name"],
                    "password": user_props["password"],
                    "role": user_props["role"],
                    "username": user_props["username"],
                }
            )

    def test_should_return_correct_data(self):
        user_props = make_fake_user()

        result = self.sut.execute(
            {
                "email": user_props["email"],
                "first_name": user_props["first_name"],
                "last_name": user_props["last_name"],
                "password": user_props["password"],
                "role": user_props["role"],
                "username": user_props["username"],
            }
        )

        assert result["email"] == user_props["email"]
        assert result["username"] == user_props["username"]
        assert result["id"] is not None

        self.repo.create.assert_called_once()
