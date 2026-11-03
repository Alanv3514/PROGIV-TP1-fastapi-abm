from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True  # default value, field becomes optional


class UpdateUser(BaseModel):
    # all fields optional: only the ones sent by the client are updated
    name: str | None = None
    is_active: bool | None = None


class GetUsersResponse(BaseModel):
    users: List[User]


class CreateUserResponse(BaseModel):
    message: str


class DeleteUserResponse(BaseModel):
    message: str
