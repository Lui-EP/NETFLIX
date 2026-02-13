from fastapi import FastAPI, HTTPException

from application.services.microservicio_a_service import MicroservicioAService
from domain.models import MicroservicioA, MicroservicioACreate, MicroservicioAUpdate
from infraestructura.adapters.microservicio_a_memory_repository import MicroservicioAMemoryRepository

app = FastAPI(title="MicroservicioA")

_repo = MicroservicioAMemoryRepository()
_service = MicroservicioAService(_repo)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "microservicio_a"}


@app.post("/microservicio-a", response_model=MicroservicioA, status_code=201)
def crear_item(payload: MicroservicioACreate) -> MicroservicioA:
    return _service.create_item(payload)


@app.get("/microservicio-a", response_model=list[MicroservicioA])
def listar_items() -> list[MicroservicioA]:
    return _service.get_items()


@app.get("/microservicio-a/{item_id}", response_model=MicroservicioA)
def obtener_item(item_id: int) -> MicroservicioA:
    item = _service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return item


@app.put("/microservicio-a/{item_id}", response_model=MicroservicioA)
def actualizar_item(item_id: int, payload: MicroservicioAUpdate) -> MicroservicioA:
    item = _service.update_item(item_id, payload)
    if not item:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return item


@app.delete("/microservicio-a/{item_id}", status_code=204)
def eliminar_item(item_id: int) -> None:
    deleted = _service.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return None
