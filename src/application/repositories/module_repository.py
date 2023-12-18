from abc import ABC, abstractmethod

from src.domain.entities.course import Module


class IModuleRepository(ABC):
    @abstractmethod
    def create(self, module: Module) -> tuple[bool, str]:
        pass

    @abstractmethod
    def get_by_id(self, module_id: str) -> Module:
        pass

    @abstractmethod
    def get_all_by_course_id(self, course_id: str) -> list[Module]:
        pass

    @abstractmethod
    def update(self, module: Module) -> tuple[bool, str]:
        pass

    @abstractmethod
    def delete(self, module_id: str) -> bool:
        pass
