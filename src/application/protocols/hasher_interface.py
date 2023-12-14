from abc import ABC, abstractmethod


class HasherInterface(ABC):
    @abstractmethod
    def hash(self, password: str) -> str:
        pass

    @abstractmethod
    def check(self, password: str, hashed_password: str) -> bool:
        pass
