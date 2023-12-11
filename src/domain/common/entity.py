from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar
from uuid import uuid4

T = TypeVar("T")


class UniqueEntityID:
    def __init__(self, id: Optional[str] = None):
        self.id = id if id else str(uuid4())

    def equals(self, other: "UniqueEntityID") -> bool:
        return self.id == other.id

    @staticmethod
    def generate() -> str:
        return str(uuid4())


class Entity(ABC, Generic[T]):
    def __init__(self, props: T, id: Optional[str] = None) -> None:
        self._id = UniqueEntityID(id)
        self.props = props

    @abstractmethod
    def equals(self, object: "Entity") -> bool:
        pass

    @property
    def id(self) -> "str":
        return self._id.id

    def get_props(self) -> T:
        return self.props
