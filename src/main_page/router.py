from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def show_main_page():
    return "RunCode main page"