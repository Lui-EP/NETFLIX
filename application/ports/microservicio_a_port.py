from abc import ABC, abstractmethod

from domain.models import MicroservicioA, MicroservicioACreate, MicroservicioAUpdate


class MicroservicioARepositoryPort(ABC):
    @abstractmethod
    def create(self, data: MicroservicioACreate) -> MicroservicioA:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[MicroservicioA]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, item_id: int) -> MicroservicioA | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id: int, data: MicroservicioAUpdate) -> MicroservicioA | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        raise NotImplementedError
