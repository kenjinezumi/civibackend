from sqlalchemy.orm import Session
from app.models.partner_form import PartnerForm
from app.models.partner_form_answer import PartnerFormAnswer
from sqlalchemy.exc import NoResultFound

class PartnerFormRepository:
    @staticmethod
    def get_by_partner_id(db: Session, partner_id: str) -> PartnerForm:
        """
        Retrieves a partner form entry by its partner_id (slug).
        """
        return db.query(PartnerForm).filter(PartnerForm.partner_id == partner_id).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> PartnerForm:
        """
        Retrieves a partner form entry by email.
        """
        return db.query(PartnerForm).filter(PartnerForm.partner_email == email).first()

    @staticmethod
    def list_by_form_id(db: Session, form_id: int):
        """
        Lists all partner forms linked to a specific form.
        """
        return db.query(PartnerForm).filter(PartnerForm.form_id == form_id).all()

    @staticmethod
    def create(db: Session, partner_form: PartnerForm) -> PartnerForm:
        """
        Creates a new partner form entry.
        """
        db.add(partner_form)
        db.commit()
        db.refresh(partner_form)
        return partner_form

    @staticmethod
    def update(db: Session, partner_form: PartnerForm) -> PartnerForm:
        """
        Updates an existing partner form entry.
        """
        db.commit()
        db.refresh(partner_form)
        return partner_form

    @staticmethod
    def delete(db: Session, partner_form: PartnerForm):
        """
        Deletes a partner form entry.
        """
        db.delete(partner_form)
        db.commit()

    @staticmethod
    def regenerate_password(db: Session, partner_form: PartnerForm, new_password: str) -> PartnerForm:
        """
        Regenerates a new password for the partner.
        """
        partner_form.password = new_password
        return PartnerFormRepository.update(db, partner_form)
