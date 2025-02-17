from fastapi import FastAPI
from src.Daily_Bot.routes import bot_router

version="v1"

app = FastAPI(
    title="webhook",
    description="learning telex",
    version="v1",
)

app.include_router(router=bot_router, prefix="", tags=["bot"])
