from unittest.mock import Mock

import pytest

from src.application.common import ApplicationError
from src.application.protocols.encrypter_interface import EncrypterInterface
from src.application.protocols.hasher_interface import HasherInterface
from src.application.use_cases.management.account.login_use_case import (
    LoginRepository,
    LoginUseCase,
)
from src.domain.entities.user import User
from src.domain.use_cases.management.account.login import Login
from tests.fixtures.mocks import make_fake_user


class TestLogin:
    sut: Login

    def setup_method(self):
        self.repo = Mock(spec=LoginRepository)
        self.hasher = Mock(spec=HasherInterface)
        self.encrypter = Mock(spec=EncrypterInterface)

        self.sut = LoginUseCase(
            repository=self.repo, hasher=self.hasher, encrypter=self.encrypter
        )

    def teardown_method(self):
        self.repo.reset_mock()

    def test_should_call_repository_with_correct_values(self):
        user_props = make_fake_user()
        user = User(user_props)

        self.repo.check_login.return_value = [True, user]
        self.hasher.check.return_value = True
        self.encrypter.encrypt.return_value = "token"

        self.sut.execute(
            {
                "email": user_props["email"],
                "password": user_props["password"],
            }
        )

        self.repo.check_login.assert_called_once()

    def test_should_raise_if_email_does_not_exist(self):
        user_props = make_fake_user()
        self.repo.check_login.return_value = [False, None]

        with pytest.raises(ApplicationError, match="Email does not exist."):
            self.sut.execute(
                {
                    "email": user_props["email"],
                    "password": user_props["password"],
                }
            )

    def test_should_raise_if_password_does_not_match(self):
        user_props = make_fake_user()
        self.repo.check_login.return_value = True, User(user_props)
        self.hasher.check.return_value = False

        with pytest.raises(ApplicationError, match="Password is incorrect"):
            self.sut.execute(
                {
                    "email": user_props["email"],
                    "password": user_props["password"],
                }
            )

    @pytest.mark.parametrize(
        "login_type",
        [({"email": "fake_email@gmail.com"}), ({"username": "fake_username"})],
    )
    def test_should_return_token(self, login_type):
        user_props = make_fake_user(
            email=login_type.get("email", None),
            username=login_type.get("username", None),
        )

        self.repo.check_login.return_value = [True, User(user_props)]
        self.hasher.check.return_value = True
        self.encrypter.encrypt.return_value = "token"

        result = self.sut.execute(
            {
                "email": user_props["email"] if "email" in login_type else "",
                "username": user_props["username"] if "username" in login_type else "",
                "password": user_props["password"],
            }
        )

        assert result["token"] is not None
        assert result["email"] == user_props["email"]
        assert result["username"] == user_props["username"]
        assert result["role"] == user_props["role"]
