from sqlalchemy import Integer, String, Enum, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Problem(Base):
    __tablename__ = "problem"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    level: Mapped[str] = mapped_column(Enum("easy", "medium", "hard", name="level_enum"), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


def create_problem_mixin(table_name):
    table = Table(
        table_name,
        Base.metadata,
        Column("input", String),
        Column("output", String)
    )
    return table
