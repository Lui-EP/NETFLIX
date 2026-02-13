from application.ports.microservicio_a_port import MicroservicioARepositoryPort
from domain.models import MicroservicioA, MicroservicioACreate, MicroservicioAUpdate


class MicroservicioAMemoryRepository(MicroservicioARepositoryPort):
    def __init__(self) -> None:
        self._items: dict[int, MicroservicioA] = {}
        self._next_id = 1

    def create(self, data: MicroservicioACreate) -> MicroservicioA:
        item = MicroservicioA(id=self._next_id, **data.model_dump())
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def get_all(self) -> list[MicroservicioA]:
        return list(self._items.values())

    def get_by_id(self, item_id: int) -> MicroservicioA | None:
        return self._items.get(item_id)

    def update(self, item_id: int, data: MicroservicioAUpdate) -> MicroservicioA | None:
        current = self._items.get(item_id)
        if not current:
            return None
        updated = current.model_copy(update=data.model_dump(exclude_unset=True))
        self._items[item_id] = updated
        return updated

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
