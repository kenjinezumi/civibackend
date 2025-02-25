# app/main.py
import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.routers.form_router import router as form_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or "http://127.0.0.1:3000"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(form_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
