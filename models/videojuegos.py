from pydantic import BaseModel
from typing import List


class Videojuego(BaseModel):
    id: int
    titulo: str
    desarrollador: str
    anio: int
    esta_disponible: bool = True


class GetVideojuegosResponse(BaseModel):
    videojuegos: List[Videojuego]


class CreateVideojuegoResponse(BaseModel):
    message: str


class UpdateVideojuego(BaseModel):
    # all fields optional: only the ones sent by the client are updated
    titulo: str | None = None
    desarrollador: str | None = None
    anio: int | None = None
    esta_disponible: bool | None = None


class DeleteVideojuegoResponse(BaseModel):
    message: str
