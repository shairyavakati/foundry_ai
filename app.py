from fastapi import FastAPI
from routers.user_router import router as user_router

app = FastAPI(
    title="Foundry AI",
    version="1.0.0"
)

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)
