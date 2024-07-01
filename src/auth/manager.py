from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.utils import get_user_db

from src.config import SECRET_AUTH as SECRET
from src.database import get_async_session, async_session_maker
from src.score_system.models import Rank
from src.score_system.utils import add_rank


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET

    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        async with async_session_maker() as session:
            await add_rank(session, user)

    async def on_after_forgot_password(

            self, user: User, token: str, request: Optional[Request] = None

    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(

            self, user: User, token: str, request: Optional[Request] = None

    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
