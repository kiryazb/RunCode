import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: int
    score: int = 0


class UserCreate(schemas.BaseUserCreate):
    id: int
    score: int = 0


class UserUpdate(schemas.BaseUserUpdate):
    id: int
    score: int = 0
