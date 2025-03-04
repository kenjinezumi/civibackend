# app/repositories/partner_form_answer_repository.py

from sqlalchemy.orm import Session
from typing import Optional
from app.models.partner_form_answer import PartnerFormAnswer

class PartnerFormAnswerRepository:
    @staticmethod
    def get_by_partner_form_id(db: Session, partner_form_id: int) -> Optional[PartnerFormAnswer]:
        return db.query(PartnerFormAnswer).filter(
            PartnerFormAnswer.partner_form_id == partner_form_id
        ).first()

    @staticmethod
    def create_or_update(
        db: Session, partner_form_id: int, answers_data: dict
    ) -> PartnerFormAnswer:
        """
        Creates or updates the single JSON answers row for a given partner_form_id.
        """
        existing = db.query(PartnerFormAnswer).filter(
            PartnerFormAnswer.partner_form_id == partner_form_id
        ).first()
        if existing:
            existing.answers_data = answers_data
            db.commit()
            db.refresh(existing)
            return existing
        else:
            new_record = PartnerFormAnswer(
                partner_form_id=partner_form_id,
                answers_data=answers_data
            )
            db.add(new_record)
            db.commit()
            db.refresh(new_record)
            return new_record
