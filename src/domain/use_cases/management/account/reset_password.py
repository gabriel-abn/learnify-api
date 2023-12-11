from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class ResetPasswordParams(TypedDict):
    id: str
    new_password: str


class ResetPasswordResult(TypedDict):
    id: str
    reseted: bool
    updated_at: str


class ResetPassword(UseCase[ResetPasswordParams, ResetPasswordResult]):
    @abstractmethod
    def execute(self, params: ResetPasswordParams) -> ResetPasswordResult:
        pass
