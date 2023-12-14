from abc import ABC, abstractmethod


class EncrypterInterface(ABC):
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass
