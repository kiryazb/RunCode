from fastapi import Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import user

from src.auth.models import User
from src.auth.schemas import UserUpdate
from src.database import get_async_session, async_session_maker
from src.score_system.models import Rank


async def add_rank(session: AsyncSession, user) -> None:
    count = await session.execute(func.count(User.id))
    rank = Rank(user_id=user.id, place=count.scalar())
    session.add(rank)
    await session.flush()
    await session.commit()


async def add_score(session: AsyncSession, user: UserUpdate) -> None:
    user_rank = await session.get(Rank, user.id)
    user_rank.score += 1
    await session.commit()


async def update_place(session: AsyncSession, user: UserUpdate) -> None:
    curr_user = await session.get(Rank, user.id)
    query = select(Rank).where(Rank.place == curr_user.place - 1)
    next_user = await session.execute(query)
    next_user = next_user.scalar()
    while next_user and curr_user.score > next_user.score:
        curr_user.place, next_user.place = next_user.place, curr_user.place
        query = select(Rank).where(Rank.place == curr_user.place - 1)
        next_user = await session.execute(query)
        next_user = next_user.scalar()
    await session.commit()
    return

