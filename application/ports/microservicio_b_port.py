from abc import ABC, abstractmethod

from domain.models import MicroservicioB, MicroservicioBCreate, MicroservicioBUpdate


class MicroservicioBRepositoryPort(ABC):
    @abstractmethod
    def create(self, data: MicroservicioBCreate) -> MicroservicioB:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[MicroservicioB]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, item_id: int) -> MicroservicioB | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id: int, data: MicroservicioBUpdate) -> MicroservicioB | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        raise NotImplementedError
