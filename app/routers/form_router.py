# app/routers/form_router.py
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.controllers.form_controller import FormController
from app.schemas.form_schema import FormCreate, FormOut, FormUpdate
from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/forms", tags=["forms"])

@router.post("/", response_model=FormOut)
def create_form(form_data: FormCreate, db: Session = Depends(get_db)):
    return FormController.create_form(db, form_data)

@router.get("/", response_model=List[FormOut])
def list_forms(db: Session = Depends(get_db)):
    return FormController.get_all_forms(db)

@router.get("/{form_id}", response_model=FormOut)
def retrieve_form(form_id: int, db: Session = Depends(get_db)):
    return FormController.get_form(db, form_id)

@router.put("/{form_id}", response_model=FormOut)
def update_form(form_id: int, updates: FormUpdate, db: Session = Depends(get_db)):
    return FormController.update_form(db, form_id, updates)

@router.delete("/{form_id}")
def delete_form(form_id: int, db: Session = Depends(get_db)):
    FormController.delete_form(db, form_id)
    return {"message": "Form deleted"}
