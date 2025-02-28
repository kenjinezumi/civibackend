# app/repositories/form_repository.py
from typing import List
from sqlalchemy.orm import Session, joinedload
from app.models.form import Form
from app.models.page import Page
from app.models.section import Section
from app.models.question import Question

class FormRepository:
    @staticmethod
    def get_by_id(db: Session, form_id: int) -> Form:
        return (
            db.query(Form)
            .options(
                joinedload(Form.pages)
                .joinedload(Page.sections)
                .joinedload(Section.questions)
            )
            .filter(Form.id == form_id)
            .first()
        )

    @staticmethod
    def get_all(db: Session) -> List[Form]:
        return (
            db.query(Form)
            .options(
                joinedload(Form.pages)
                .joinedload(Page.sections)
                .joinedload(Section.questions)
            )
            .all()
        )

    @staticmethod
    def create(db: Session, form_obj: Form) -> Form:
        db.add(form_obj)
        db.commit()
        db.refresh(form_obj)
        return form_obj

    @staticmethod
    def save(db: Session, form_obj: Form) -> Form:
        db.commit()
        db.refresh(form_obj)
        return form_obj

    @staticmethod
    def delete(db: Session, form_obj: Form) -> None:
        db.delete(form_obj)
        db.commit()
