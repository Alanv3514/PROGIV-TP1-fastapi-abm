from fastapi import APIRouter
from models.videojuegos import Videojuego, GetVideojuegosResponse

router = APIRouter()

videojuegos: list[Videojuego] = []


@router.get("/videojuego")
def get_videojuegos(esta_disponible: bool | None = None) -> GetVideojuegosResponse:
    if esta_disponible is None:
        result = videojuegos
    else:
        result = [v for v in videojuegos if v.esta_disponible == esta_disponible]
    return GetVideojuegosResponse(videojuegos=result)
