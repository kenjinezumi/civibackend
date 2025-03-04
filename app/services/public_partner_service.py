import bcrypt
from sqlalchemy.orm import Session
from app.repositories.partner_form_repository import PartnerFormRepository
from app.models.partner_form import PartnerForm
from app.models.partner_form_answer import PartnerFormAnswer

class PublicPartnerService:
    @staticmethod
    def authenticate_partner(db: Session, partner_id: str, email: str, password: str) -> PartnerForm:
        """
        Authenticate a partner by matching email and password.
        """
        # Fetch the partner form by partner_id
        pf = PartnerFormRepository.get_by_partner_id(db, partner_id)
        if not pf:
            raise ValueError("Partner form not found")

        # Validate email and password
        if pf.partner_email.lower() != email.lower():
            raise ValueError("Invalid email")
        if pf.password != password:
            raise ValueError("Invalid password")

        return pf
        """
        Authenticate a partner by matching email and password.
        """
        # Fetch the partner form by partner_id
        pf = PartnerFormRepository.get_by_partner_id(db, partner_id)
        if not pf:
            raise ValueError("Partner form not found")

        # Validate email and password
        if pf.partner_email.lower() != email.lower():
            raise ValueError("Invalid email")
        if pf.password != password:
            raise ValueError("Invalid password")

        return pf
        """
        Authenticates a partner using partner_id, email, and password.
        """
        print(f"[DEBUG] Authenticating partner_id={partner_id}, email={email}")

        partner_form = PartnerFormRepository.get_by_partner_id(db, partner_id)
        
        if not partner_form:
            print(f"[ERROR] No partner form found for partner_id={partner_id}")
            raise ValueError("Invalid partner ID.")
        
        print(f"[DEBUG] Found partner: {partner_form.partner_email}")

        if partner_form.partner_email.lower() != email.lower():
            print(f"[ERROR] Email does not match! Expected {partner_form.partner_email}, got {email}")
            raise ValueError("Invalid email.")

        if not bcrypt.checkpw(password.encode("utf-8"), partner_form.password.encode("utf-8")):
            print(f"[ERROR] Password does not match!")
            raise ValueError("Invalid password.")

        print(f"[SUCCESS] Partner authenticated: {partner_form.partner_email}")
        return partner_form

    @staticmethod
    def save_answers(db: Session, partner_id: str, answers: dict) -> PartnerFormAnswer:
        """
        Saves the answers submitted by a partner for a form.
        """
        partner_form = PartnerFormRepository.get_by_partner_id(db, partner_id)
        if not partner_form:
            raise ValueError("Invalid partner ID.")

        new_answers = PartnerFormAnswer(partner_form_id=partner_form.id, answers_data=answers)
        db.add(new_answers)
        db.commit()
        db.refresh(new_answers)
        return new_answers
