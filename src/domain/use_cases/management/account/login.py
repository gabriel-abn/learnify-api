from abc import abstractmethod
from typing import Required, TypedDict

from src.domain.common.use_case import UseCase


class LoginParams(TypedDict, total=False):
    username: str
    email: str
    password: Required[str]


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
