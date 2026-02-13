from application.ports.microservicio_b_port import MicroservicioBRepositoryPort
from domain.models import MicroservicioB, MicroservicioBCreate, MicroservicioBUpdate


class MicroservicioBService:
    def __init__(self, repository: MicroservicioBRepositoryPort) -> None:
        self.repository = repository

    def create_item(self, data: MicroservicioBCreate) -> MicroservicioB:
        return self.repository.create(data)

    def get_items(self) -> list[MicroservicioB]:
        return self.repository.get_all()

    def get_item(self, item_id: int) -> MicroservicioB | None:
        return self.repository.get_by_id(item_id)

    def update_item(self, item_id: int, data: MicroservicioBUpdate) -> MicroservicioB | None:
        return self.repository.update(item_id, data)

    def delete_item(self, item_id: int) -> bool:
        return self.repository.delete(item_id)
