from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    UpdateUser,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez", is_active=False),
]


@router.get("/user")
def get_users(is_active: bool | None = None) -> GetUsersResponse:
    if is_active is None:
        result = usuarios
    else:
        result = [u for u in usuarios if u.is_active == is_active]
    return GetUsersResponse(users=result)


@router.put("/user/{id}")
def update_user(id: int, updates: UpdateUser) -> User:
    user = next((u for u in usuarios if u.id == id), None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    if updates.name is not None:
        user.name = updates.name
    if updates.is_active is not None:
        user.is_active = updates.is_active
    return user


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="ususario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")
