# app/services/form_service.py
from sqlalchemy.orm import Session
from app.repositories.form_repository import FormRepository
from app.models.form import Form
from app.models.section import Section
from app.models.question import Question
from app.schemas.form_schema import FormCreate, FormUpdate

class FormService:
    @staticmethod
    def create_form(db: Session, form_data: FormCreate) -> Form:
        # Build a Form object with nested sections/questions
        form_obj = Form(
            title=form_data.title,
            description=form_data.description,
            published=form_data.published
        )

        for sec_data in form_data.sections:
            sec_obj = Section(title=sec_data.title)
            for q_data in sec_data.questions:
                q_obj = Question(
                    label=q_data.label,
                    type=q_data.type,
                    required=q_data.required
                )
                sec_obj.questions.append(q_obj)

            form_obj.sections.append(sec_obj)

        return FormRepository.create(db, form_obj)

    @staticmethod
    def get_form(db: Session, form_id: int) -> Form:
        return FormRepository.get_by_id(db, form_id)

    @staticmethod
    def get_all_forms(db: Session):
        return FormRepository.get_all(db)

    @staticmethod
    def update_form(db: Session, form_id: int, updates: FormUpdate) -> Form:
        form_obj = FormRepository.get_by_id(db, form_id)
        if not form_obj:
            raise ValueError("Form not found")

        if updates.title is not None:
            form_obj.title = updates.title
        if updates.description is not None:
            form_obj.description = updates.description
        if updates.published is not None:
            form_obj.published = updates.published

        return FormRepository.save(db, form_obj)

    @staticmethod
    def delete_form(db: Session, form_id: int) -> None:
        form_obj = FormRepository.get_by_id(db, form_id)
        if not form_obj:
            raise ValueError("Form not found")
        FormRepository.delete(db, form_obj)
