# app/main.py
import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.routers.form_router import router as form_router
from app.routers.partner_form_router import router as partner_router
from app.routers.public_partner_router import router as public_partner_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
     "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000"
        "http://192.168.0.37:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(form_router)
app.include_router(partner_router)
app.include_router(partner_router)
app.include_router(public_partner_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
