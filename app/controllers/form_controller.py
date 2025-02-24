# app/controllers/form_controller.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.services.form_service import FormService
from app.schemas.form_schema import FormCreate, FormUpdate

class FormController:
    @staticmethod
    def create_form(db: Session, form_data: FormCreate):
        try:
            return FormService.create_form(db, form_data)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    @staticmethod
    def get_form(db: Session, form_id: int):
        form_obj = FormService.get_form(db, form_id)
        if not form_obj:
            raise HTTPException(status_code=404, detail="Form not found")
        return form_obj

    @staticmethod
    def get_all_forms(db: Session):
        return FormService.get_all_forms(db)

    @staticmethod
    def update_form(db: Session, form_id: int, updates: FormUpdate):
        try:
            return FormService.update_form(db, form_id, updates)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    @staticmethod
    def delete_form(db: Session, form_id: int):
        try:
            return FormService.delete_form(db, form_id)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
