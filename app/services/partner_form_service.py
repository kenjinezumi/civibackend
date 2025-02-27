from sqlalchemy.orm import Session
from app.models.partner_form import PartnerForm
from app.repositories.partner_form_repository import PartnerFormRepository
from app.schemas.partner_form_schema import PartnerFormCreate

import uuid

class PartnerFormService:
    @staticmethod
    def create_partner_form(db: Session, data: PartnerFormCreate) -> PartnerForm:
        # Possibly auto-generate a unique slug if not provided
        # e.g. use a random UUID
        slug = data.public_url if data.public_url else str(uuid.uuid4())[:8]

        pf_obj = PartnerForm(
            form_id=data.form_id,
            partner_id=data.partner_id,
            partner_name=data.partner_name,
            partner_email=data.partner_email,
            public_url=slug,
            completion_percentage=data.completion_percentage
        )
        return PartnerFormRepository.create(db, pf_obj)

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> PartnerForm:
        return PartnerFormRepository.get_by_slug(db, slug)

    @staticmethod
    def update_completion(db: Session, slug: str, new_completion: float) -> PartnerForm:
        pf_obj = PartnerFormRepository.get_by_slug(db, slug)
        if not pf_obj:
            raise ValueError("Published form not found")
        pf_obj.completion_percentage = new_completion
        return PartnerFormRepository.save(db, pf_obj)
