# app/services/form_service.py
from sqlalchemy.orm import Session
from app.repositories.form_repository import FormRepository
from app.models.form import Form
from app.models.page import Page
from app.models.section import Section
from app.models.question import Question
from app.schemas.form_schema import FormCreate, FormUpdate, QuestionCreate

class FormService:
    @staticmethod
    def create_form(db: Session, form_data: FormCreate) -> Form:
        form_obj = Form(
            title=form_data.title,
            description=form_data.description,
            published=form_data.published,
            country=form_data.country,
            created_by=form_data.created_by
        )

        # Build each Page
        for page_data in form_data.pages:
            page_obj = Page(
                title=page_data.title,
                description=page_data.description
            )

            # If you want unsectioned:
            # for q_data in page_data.unsectioned:
            #     q_obj = Question(
            #         label=q_data.label,
            #         type=q_data.type,
            #         required=q_data.required,
            #         placeholder=q_data.placeholder,
            #         helpText=q_data.helpText,
            #         choices=q_data.choices,       # store in JSON
            #         skip_logic=(q_data.skipLogic.dict() if q_data.skipLogic else None)
            #     )
            #     # you'd also do q_obj.page_id = page_obj.id if needed, or use relationship

            # For each section
            for sec_data in page_data.sections:
                sec_obj = Section(title=sec_data.title)
                for q_data in sec_data.questions:
                    q_obj = Question(
                        label=q_data.label,
                        type=q_data.type,
                        required=q_data.required,
                        placeholder=q_data.placeholder,
                        helpText=q_data.helpText,
                        choices=q_data.choices,  # stored in JSON column
                        skip_logic=(q_data.skipLogic.dict() if q_data.skipLogic else None)
                    )
                    sec_obj.questions.append(q_obj)
                page_obj.sections.append(sec_obj)

            form_obj.pages.append(page_obj)

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

        # Update top-level
        if updates.title is not None:
            form_obj.title = updates.title
        if updates.description is not None:
            form_obj.description = updates.description
        if updates.published is not None:
            form_obj.published = updates.published
        if updates.country is not None:
            form_obj.country = updates.country
        if updates.created_by is not None:
            form_obj.created_by = updates.created_by

        # Full replace of pages
        if updates.pages is not None:
            form_obj.pages.clear()
            for page_data in updates.pages:
                page_obj = Page(
                    title=page_data.title,
                    description=page_data.description
                )

                # unsectioned if needed
                # for q_data in page_data.unsectioned:
                #    ...

                for sec_data in page_data.sections:
                    sec_obj = Section(title=sec_data.title)
                    for q_data in sec_data.questions:
                        q_obj = Question(
                            label=q_data.label,
                            type=q_data.type,
                            required=q_data.required,
                            placeholder=q_data.placeholder,
                            helpText=q_data.helpText,
                            choices=q_data.choices,
                            skip_logic=(q_data.skipLogic.dict() if q_data.skipLogic else None)
                        )
                        sec_obj.questions.append(q_obj)
                    page_obj.sections.append(sec_obj)

                form_obj.pages.append(page_obj)

        return FormRepository.save(db, form_obj)

    @staticmethod
    def delete_form(db: Session, form_id: int) -> None:
        form_obj = FormRepository.get_by_id(db, form_id)
        if not form_obj:
            raise ValueError("Form not found")
        FormRepository.delete(db, form_obj)
