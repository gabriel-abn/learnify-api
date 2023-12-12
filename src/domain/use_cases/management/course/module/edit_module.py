from abc import abstractmethod
from typing import TypedDict

from src.domain.common.use_case import UseCase


class EditModuleParams(TypedDict):
    course_id: str
    module_id: str
    name: str
    description: str


class EditModuleResult(TypedDict):
    module_id: str
    updated_at: str


class EditModule(UseCase[EditModuleParams, EditModuleResult]):
    @abstractmethod
    def execute(self, params: EditModuleParams) -> EditModuleResult:
        pass
