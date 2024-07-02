from fastapi import APIRouter, Depends, HTTPException

from src.auth.config import fastapi_users
from src.auth.models import User
from src.problems_system.utils import check_solution

router = APIRouter(
    prefix="/problems",
    tags=["problems"]
)

current_user = fastapi_users.current_user()


@router.get("/{problem_name}")
async def show_problem_page(problem_name: str):
    return f"{problem_name}"

@router.post("/{problem_name}")
async def send_problem_solution(problem_name: str, solution: str, user: User = Depends(current_user)):
    print("dfdf")
    if await check_solution(solution):
        print(user.id)
    return {"status": "success"}
