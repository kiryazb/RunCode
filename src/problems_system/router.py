from typing import Dict

from fastapi import APIRouter, Depends

from src.auth.config import fastapi_users
from src.auth.schemas import UserUpdate
from src.database import get_async_session
from src.problems_system.problems_checker import check_solution
from src.score_system.utils import add_score, update_place

router = APIRouter(
    prefix="/problems",
    tags=["problems"]
)

current_user = fastapi_users.current_user()


@router.get("/{problem_name}")
async def show_problem_page(problem_name: str):
    return f"{problem_name}"


@router.post("/{problem_name}")
async def send_problem_solution(
        problem_name: str, solution: str, user: UserUpdate = Depends(current_user), session=Depends(get_async_session)
) -> Dict[str, str]:
    if await check_solution(solution, problem_name, session):
        await add_score(session, user)
        await update_place(session, user)
    return {"status": "success"}
