from abc import abstractmethod
from typing import Required, TypedDict

from src.domain.common.use_case import UseCase


class UpdateProfileParams(TypedDict, total=False):
    id: Required[str]
    username: str
    first_name: str
    last_name: str


class UpdateProfileResult(TypedDict):
    id: str
    username: str
    first_name: str
    last_name: str
    updated_at: str


class UpdateProfile(UseCase[UpdateProfileParams, UpdateProfileResult]):
    @abstractmethod
    def execute(self, params: UpdateProfileParams) -> UpdateProfileResult:
        pass
