from application.ports.microservicio_b_port import MicroservicioBRepositoryPort
from domain.models import MicroservicioB, MicroservicioBCreate, MicroservicioBUpdate


class MicroservicioBMemoryRepository(MicroservicioBRepositoryPort):
    def __init__(self) -> None:
        self._items: dict[int, MicroservicioB] = {}
        self._next_id = 1

    def create(self, data: MicroservicioBCreate) -> MicroservicioB:
        item = MicroservicioB(id=self._next_id, **data.model_dump())
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def get_all(self) -> list[MicroservicioB]:
        return list(self._items.values())

    def get_by_id(self, item_id: int) -> MicroservicioB | None:
        return self._items.get(item_id)

    def update(self, item_id: int, data: MicroservicioBUpdate) -> MicroservicioB | None:
        current = self._items.get(item_id)
        if not current:
            return None
        updated = current.model_copy(update=data.model_dump(exclude_unset=True))
        self._items[item_id] = updated
        return updated

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
