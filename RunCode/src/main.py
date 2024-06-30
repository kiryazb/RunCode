import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from .auth.config import auth_backend
from .auth.manager import get_user_manager
from .auth.models import User
from .auth.schemas import UserRead, UserCreate

from .main_page.router import router as main_page_router

app = FastAPI(
    title="RunCode"
)


app.include_router(main_page_router)


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

