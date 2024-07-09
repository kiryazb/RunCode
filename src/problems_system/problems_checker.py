from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.problems_system.models import create_problem_mixin


async def run_solution(code, input, output, arguments):
    locals_ = dict(zip(arguments, input.split(" & ")))
    return exec(code, locals_) == output


async def check_solution(code: str, table_name: str, session: AsyncSession):
    table = create_problem_mixin(table_name)
    query = select(table)
    result = await session.execute(query)
    tests = result.fetchall()
    for test in tests:
        inp, output, arguments = test[0], test[1], test[2].split()
        if not await run_solution(code, inp, output, arguments):
            return False
    return True
