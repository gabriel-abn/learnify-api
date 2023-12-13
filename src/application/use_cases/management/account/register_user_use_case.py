from abc import ABC, abstractmethod

from src.application.common import ApplicationError
from src.domain.entities.user import User
from src.domain.use_cases.management.account.register_user import (
    RegisterUser,
    RegisterUserParams,
    RegisterUserResult,
)

EMAIL_ALREADY_EXISTS = "INVALID_EMAIL", "Email already exists."
USERNAME_ALREADY_EXISTS = "INVALID_USERNAME", "Username already exists."
USER_NOT_CREATED = "USER_NOT_CREATED", "User not created."


class RegisterUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> bool:
        pass

    @abstractmethod
    def check_email_exists(self, email: str) -> bool:
        pass

    @abstractmethod
    def check_username_exists(self, username: str) -> bool:
        pass


class RegisterUserUseCase(RegisterUser):
    def __init__(self, repository: RegisterUserRepository) -> None:
        self.repository = repository

    def execute(self, params: RegisterUserParams) -> RegisterUserResult:
        if self.repository.check_email_exists(params["email"]):
            raise ApplicationError(EMAIL_ALREADY_EXISTS)

        if self.repository.check_username_exists(params["username"]):
            raise ApplicationError(USERNAME_ALREADY_EXISTS)

        user = User(
            {
                "email": params["email"],
                "first_name": params["first_name"],
                "last_name": params["last_name"],
                "password": params["password"],
                "role": params["role"],
                "username": params["username"],
            }
        )

        created = self.repository.create(user)

        if not created:
            raise ApplicationError(USER_NOT_CREATED)

        return {
            "id": user.id,
            "email": user.props["email"],
            "username": user.props["username"],
        }
