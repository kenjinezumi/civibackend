# app/services/partner_form_service.py

import uuid
import secrets
from typing import List
from sqlalchemy.orm import Session

from app.repositories.partner_form_repository import PartnerFormRepository
from app.models.partner_form import PartnerForm
from app.schemas.partner_form_schema import PartnerFormCreate, PartnerFormUpdate

class PartnerFormService:
    @staticmethod
    def list_for_form(db: Session, form_id: int) -> List[PartnerForm]:
        """Return all partner_form records that belong to a specific form."""
        return PartnerFormRepository.list_by_form_id(db, form_id)

    @staticmethod
    def create_partner_form(db: Session, form_id: int, data: PartnerFormCreate) -> PartnerForm:
        """
        Create a new PartnerForm record for the given form_id.
        We'll generate a unique partner_id if not given,
        and we'll generate a random password if not provided.
        """

        # If you want a short random slug for partner_id:
        # Or let them pass partner_id in the request if you want
        new_partner_id = str(uuid.uuid4())[:8]

        # If no password is provided, generate a random one:
        # (In real usage, you'd want a hashed password.)
        new_password = data.password or secrets.token_urlsafe(6)

        pf_obj = PartnerForm(
            form_id=form_id,
            partner_id=new_partner_id,
            partner_name=data.partner_name,
            partner_email=data.partner_email,
            password=new_password,
            completion_percentage=data.completion_percentage or 0.0
        )
        return PartnerFormRepository.create(db, pf_obj)

    @staticmethod
    def update_partner_form(db: Session, pf_id: int, updates: PartnerFormUpdate) -> PartnerForm:
        """Update an existing participant's record (name, email, password, completion, etc.)."""
        pf_obj = PartnerFormRepository.get_by_id(db, pf_id)
        if not pf_obj:
            raise ValueError("Participant not found")

        if updates.partner_name is not None:
            pf_obj.partner_name = updates.partner_name
        if updates.partner_email is not None:
            pf_obj.partner_email = updates.partner_email
        if updates.password is not None:
            pf_obj.password = updates.password  # or hash it
        if updates.completion_percentage is not None:
            pf_obj.completion_percentage = updates.completion_percentage

        return PartnerFormRepository.save(db, pf_obj)

    @staticmethod
    def delete_partner_form(db: Session, pf_id: int) -> None:
        """Delete a participant record."""
        pf_obj = PartnerFormRepository.get_by_id(db, pf_id)
        if not pf_obj:
            raise ValueError("Participant not found")
        PartnerFormRepository.delete(db, pf_obj)

    @staticmethod
    def get_partner_form_by_id(db: Session, pf_id: int) -> PartnerForm:
        return PartnerFormRepository.get_by_id(db, pf_id)