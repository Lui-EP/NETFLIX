from application.ports.microservicio_a_port import MicroservicioARepositoryPort
from domain.models import MicroservicioA, MicroservicioACreate, MicroservicioAUpdate


class MicroservicioAService:
    def __init__(self, repository: MicroservicioARepositoryPort) -> None:
        self.repository = repository

    def create_item(self, data: MicroservicioACreate) -> MicroservicioA:
        return self.repository.create(data)

    def get_items(self) -> list[MicroservicioA]:
        return self.repository.get_all()

    def get_item(self, item_id: int) -> MicroservicioA | None:
        return self.repository.get_by_id(item_id)

    def update_item(self, item_id: int, data: MicroservicioAUpdate) -> MicroservicioA | None:
        return self.repository.update(item_id, data)

    def delete_item(self, item_id: int) -> bool:
        return self.repository.delete(item_id)
