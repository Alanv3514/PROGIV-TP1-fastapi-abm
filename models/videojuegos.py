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
