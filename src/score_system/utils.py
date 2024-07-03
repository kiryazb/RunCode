from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import user

from src.auth.models import User
from src.score_system.models import Rank


async def add_rank(session: AsyncSession, user) -> None:
    count = await session.execute(func.count(User.id))
    rank = Rank(user_id=user.id, place=count.scalar())
    session.add(rank)
    await session.flush()
    await session.commit()


async def add_score(session: AsyncSession, user: User) -> None:
    user = await session.get(User, user.id)
    user.score += 1
    await session.commit()


async def update_place(session: AsyncSession, user: User) -> None:
    pass
