from fastapi_users_db_sqlalchemy import UUID_ID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

from src.auth.models import User


class Base(DeclarativeBase):
    pass


class Rank(Base):
    __tablename__ = "rank"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(User.id), primary_key=True, index=True, nullable=False
    )

    place: Mapped[int] = mapped_column(
        nullable=False
    )


