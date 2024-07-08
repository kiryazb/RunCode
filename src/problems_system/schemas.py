from enum import Enum

from pydantic import BaseModel


class LevelEnum(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class Problem(BaseModel):
    id: int
    name: str
    level: LevelEnum
    description: str

    class Config:
        use_enum_values = True
