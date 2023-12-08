from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Params = TypeVar("Params")
Result = TypeVar("Result")


class UseCase(ABC, Generic[Params, Result]):
    @abstractmethod
    def execute(self, params: Params) -> Result:
        pass
