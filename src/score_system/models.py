from fastapi_users_db_sqlalchemy import UUID_ID
from sqlalchemy import ForeignKey, Integer, Index
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

from src.auth.models import User


class Base(DeclarativeBase):
    pass


class Rank(Base):
    __tablename__ = "rank"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(User.id), primary_key=True, index=True, nullable=False
    )

    score: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0
    )

    place: Mapped[int] = mapped_column(
        nullable=False
    )

    __table_args__ = (
        Index('idx_rank_score', 'score', unique=False),
    )


