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