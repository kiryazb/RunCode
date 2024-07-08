import uuid

from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

from .auth.config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate

from .main_page.router import router as main_page_router
from .problems_system.router import router as problems_system_router
from .admin_panel.router import router as admin_panel_router

app = FastAPI(
    title="RunCode",
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 401:
        print("Redirect soon..")
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"}
        )
    else:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )


app.include_router(main_page_router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    problems_system_router
)

app.include_router(
    admin_panel_router
)
