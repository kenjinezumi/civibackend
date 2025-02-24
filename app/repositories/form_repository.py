# app/repositories/form_repository.py
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.form import Form

class FormRepository:
    @staticmethod
    def create(db: Session, form_obj: Form) -> Form:
        db.add(form_obj)
        db.commit()
        db.refresh(form_obj)
        return form_obj

    @staticmethod
    def get_by_id(db: Session, form_id: int) -> Optional[Form]:
        return db.query(Form).filter(Form.id == form_id).first()

    @staticmethod
    def get_all(db: Session) -> List[Form]:
        return db.query(Form).all()

    @staticmethod
    def delete(db: Session, form_obj: Form) -> None:
        db.delete(form_obj)
        db.commit()

    @staticmethod
    def save(db: Session, form_obj: Form) -> Form:
        db.commit()
        db.refresh(form_obj)
        return form_obj
