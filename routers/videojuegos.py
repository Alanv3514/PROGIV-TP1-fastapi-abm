from fastapi import APIRouter, HTTPException, status
from models.videojuegos import (
    Videojuego,
    GetVideojuegosResponse,
    CreateVideojuegoResponse,
)

router = APIRouter()

videojuegos: list[Videojuego] = []


@router.get("/videojuego")
def get_videojuegos(esta_disponible: bool | None = None) -> GetVideojuegosResponse:
    if esta_disponible is None:
        result = videojuegos
    else:
        result = [v for v in videojuegos if v.esta_disponible == esta_disponible]
    return GetVideojuegosResponse(videojuegos=result)


@router.post("/videojuego")
def create_videojuego(videojuego: Videojuego) -> CreateVideojuegoResponse:
    videojuegos.append(videojuego)
    return CreateVideojuegoResponse(message="videojuego creado")


@router.get("/videojuego/{id}")
def get_videojuego(id: int) -> Videojuego:
    videojuego = next((v for v in videojuegos if v.id == id), None)
    if videojuego is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Videojuego no encontrado"
        )
    return videojuego
