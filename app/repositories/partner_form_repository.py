from sqlalchemy.orm import Session
from app.models.partner_form import PartnerForm

class PartnerFormRepository:
    @staticmethod
    def create(db: Session, pf_obj: PartnerForm) -> PartnerForm:
        db.add(pf_obj)
        db.commit()
        db.refresh(pf_obj)
        return pf_obj

    @staticmethod
    def get_by_id(db: Session, pf_id: int) -> PartnerForm:
        return db.query(PartnerForm).filter(PartnerForm.id == pf_id).first()

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> PartnerForm:
        return db.query(PartnerForm).filter(PartnerForm.public_url == slug).first()

    @staticmethod
    def save(db: Session, pf_obj: PartnerForm) -> PartnerForm:
        db.add(pf_obj)
        db.commit()
        db.refresh(pf_obj)
        return pf_obj

    @staticmethod
    def delete(db: Session, pf_obj: PartnerForm) -> None:
        db.delete(pf_obj)
        db.commit()
