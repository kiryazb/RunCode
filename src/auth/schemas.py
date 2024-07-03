import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: int


class UserCreate(schemas.BaseUserCreate):
    id: int


class UserUpdate(schemas.BaseUserUpdate):
    id: int
