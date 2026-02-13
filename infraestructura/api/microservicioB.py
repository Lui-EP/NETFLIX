from fastapi import FastAPI, HTTPException

from application.services.microservicio_b_service import MicroservicioBService
from domain.models import MicroservicioB, MicroservicioBCreate, MicroservicioBUpdate
from infraestructura.adapters.microservicio_b_memory_repository import MicroservicioBMemoryRepository

app = FastAPI(title="MicroservicioB")

_repo = MicroservicioBMemoryRepository()
_service = MicroservicioBService(_repo)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "microservicio_b"}


@app.post("/microservicio-b", response_model=MicroservicioB, status_code=201)
def crear_item(payload: MicroservicioBCreate) -> MicroservicioB:
    return _service.create_item(payload)


@app.get("/microservicio-b", response_model=list[MicroservicioB])
def listar_items() -> list[MicroservicioB]:
    return _service.get_items()


@app.get("/microservicio-b/{item_id}", response_model=MicroservicioB)
def obtener_item(item_id: int) -> MicroservicioB:
    item = _service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return item


@app.put("/microservicio-b/{item_id}", response_model=MicroservicioB)
def actualizar_item(item_id: int, payload: MicroservicioBUpdate) -> MicroservicioB:
    item = _service.update_item(item_id, payload)
    if not item:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return item


@app.delete("/microservicio-b/{item_id}", status_code=204)
def eliminar_item(item_id: int) -> None:
    deleted = _service.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return None
