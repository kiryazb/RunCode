from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import selectinload

from src.auth.config import fastapi_users
from src.auth.models import User
from src.database import async_session_maker
from src.problems_system.utils import check_solution
from src.score_system.utils import add_score

router = APIRouter(
    prefix="/problems",
    tags=["problems"]
)

current_user = fastapi_users.current_user()


@router.get("/{problem_name}")
async def show_problem_page(problem_name: str):
    return f"{problem_name}"

@router.post("/{problem_name}")
async def send_problem_solution(problem_name: str, solution: str, user: User = Depends(current_user)) -> Dict[str]:
    print("dfdf")
    if await check_solution(solution):
        async with async_session_maker() as session:
            await add_score(session, user)
    return {"status": "success"}
