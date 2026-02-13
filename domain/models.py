from pydantic import BaseModel, Field


class MicroservicioABase(BaseModel):
    perfiles: str = Field(..., min_length=1, max_length=120)
    idioma: str = Field(..., min_length=1, max_length=50)
    calidad: str = Field(..., min_length=1, max_length=50)


class MicroservicioACreate(MicroservicioABase):
    pass


class MicroservicioAUpdate(BaseModel):
    perfiles: str | None = Field(default=None, min_length=1, max_length=120)
    idioma: str | None = Field(default=None, min_length=1, max_length=50)
    calidad: str | None = Field(default=None, min_length=1, max_length=50)


class MicroservicioA(MicroservicioABase):
    id: int


class MicroservicioBBase(BaseModel):
    metodoPagoPredeterminado: str = Field(..., min_length=1, max_length=80)
    historialFacturas: str = Field(..., min_length=1, max_length=255)
    fechaProximoPago: str = Field(..., min_length=1, max_length=30)


class MicroservicioBCreate(MicroservicioBBase):
    pass


class MicroservicioBUpdate(BaseModel):
    metodoPagoPredeterminado: str | None = Field(default=None, min_length=1, max_length=80)
    historialFacturas: str | None = Field(default=None, min_length=1, max_length=255)
    fechaProximoPago: str | None = Field(default=None, min_length=1, max_length=30)


class MicroservicioB(MicroservicioBBase):
    id: int
