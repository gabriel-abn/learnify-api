from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class LoginParams(TypedDict):
    username: str
    email: str
    password: str


class LoginResult(TypedDict):
    id: str
    username: str
    email: str
    role: str
    token: str


class Login(UseCase[LoginParams, LoginResult]):
    @abstractmethod
    def execute(self, params: LoginParams) -> LoginResult:
        pass
