# app/main.py
import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.routers.form_router import router as form_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(form_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
