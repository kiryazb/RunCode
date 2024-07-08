from typing import Dict

from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.ddl import CreateTable

from src.database import get_async_session, engine
from src.problems_system.models import Base, create_problem_mixin, Problem
from src.problems_system.schemas import Problem as pydantic_Problem

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.post("/add_problem")
async def add_problem(request: pydantic_Problem, session: AsyncSession = Depends(get_async_session)) -> dict[
    str, str | int]:
    query = insert(Problem).values(id=request.id, name=request.name, level=request.level,
                                   description=request.description)
    await session.execute(query)
    await session.commit()
    return {"status": "success",
            "id": request.id,
            "name": request.name,
            "level": request.level,
            "description": request.description}


@router.post("/create_tests_table")
async def create_tests_table(table_name: str, session: AsyncSession = Depends(get_async_session)) -> Dict[str, str]:
    table = create_problem_mixin(table_name)
    query = CreateTable(table)
    await session.execute(query)
    await session.commit()
    return {"status": "success"}


@router.post("/add_test")
async def add_test(
        table_name: str,
        input: str,
        output: str,
        session: AsyncSession = Depends(get_async_session)) -> Dict[str, str]:
    query = insert(create_problem_mixin(table_name)).values(input=input, output=output)
    await session.execute(query)
    await session.commit()
    return {"status": "success"}
