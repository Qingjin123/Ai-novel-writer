# new-AI-novel/backend/main.py
from fastapi import FastAPI

app = FastAPI(title="AI Novel Writer Backend", version="0.1.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Novel Writer Backend!"}

@app.get("/api/v1/ping")
async def ping_pong():
    return {"ping": "pong!"}

# 更多的API端点将在这里定义