from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class RegisterUserParams(TypedDict):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    role: str


class RegisterUserResult(TypedDict):
    id: str
    username: str
    email: str


class RegisterUser(UseCase[RegisterUserParams, RegisterUserResult]):
    @abstractmethod
    def execute(self, params: RegisterUserParams) -> RegisterUserResult:
        pass
