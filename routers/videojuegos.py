from fastapi import APIRouter, HTTPException, status
from models.videojuegos import (
    Videojuego,
    UpdateVideojuego,
    GetVideojuegosResponse,
    CreateVideojuegoResponse,
    DeleteVideojuegoResponse,
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


@router.put("/videojuego/{id}")
def update_videojuego(id: int, updates: UpdateVideojuego) -> Videojuego:
    videojuego = next((v for v in videojuegos if v.id == id), None)
    if videojuego is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Videojuego no encontrado"
        )

    if updates.titulo is not None:
        videojuego.titulo = updates.titulo
    if updates.desarrollador is not None:
        videojuego.desarrollador = updates.desarrollador
    if updates.anio is not None:
        videojuego.anio = updates.anio
    if updates.esta_disponible is not None:
        videojuego.esta_disponible = updates.esta_disponible
    return videojuego


@router.delete("/videojuego/{id}")
def delete_videojuego(id: int) -> DeleteVideojuegoResponse:
    videojuego = next((v for v in videojuegos if v.id == id), None)
    if videojuego is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Videojuego no encontrado"
        )
    videojuegos.remove(videojuego)
    return DeleteVideojuegoResponse(message="videojuego borrado")
