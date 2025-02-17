from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.Daily_Bot.routes import bot_router

version="v1"

app = FastAPI(
    title="webhook",
    description="learning telex",
    version="v1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=bot_router, prefix="", tags=["bot"])
