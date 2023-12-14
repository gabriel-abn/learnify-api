from abc import ABC, abstractmethod
from typing import Optional

from src.application.common.application_error import ApplicationError
from src.application.protocols import EncrypterInterface, HasherInterface
from src.domain.entities.user import User
from src.domain.use_cases.management.account.login import (
    Login,
    LoginParams,
    LoginResult,
)

INVALID_EMAIL = "INVALID_EMAIL", "Email does not exist."
INVALID_PASSWORD = "INVALID_PASSWORD", "Password is incorrect."


class LoginRepository(ABC):
    @abstractmethod
    def check_login(
        self, email: Optional[str], username: Optional[str]
    ) -> tuple[bool, User]:
        """
        Args:
            email (Optional[str]): User email
            username (Optional[str]): Username

        Returns:
            tuple[bool, User]: (user_exists, user)
        """
        pass


class LoginUseCase(Login):
    def __init__(
        self,
        repository: LoginRepository,
        hasher: HasherInterface,
        encrypter: EncrypterInterface,
    ) -> None:
        self.repository = repository
        self.hasher = hasher
        self.encrypter = encrypter

    def execute(self, params: LoginParams) -> LoginResult:
        token: str = ""
        account = self.repository.check_login(
            email=params.get("email", None),
            username=params.get("username", None),
        )

        if account[0]:
            user = account[1]

            valid_password = self.hasher.check(
                password=params["password"], hashed_password=user.props["password"]
            )

            if not valid_password:
                raise ApplicationError(INVALID_PASSWORD)

            token = self.encrypter.encrypt(user.id)

            return {
                "id": user.id,
                "email": user.props["email"],
                "username": user.props["username"],
                "role": user.props["role"],
                "token": token,
            }

        raise ApplicationError(INVALID_EMAIL)
