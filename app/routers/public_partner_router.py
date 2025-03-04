from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.public_partner_service import PublicPartnerService
from app.schemas.partner_form_schema import PartnerFormOut
from app.schemas.answer_schema import PartnerFormAnswerCreate
from app.schemas.auth_schema import PartnerLoginRequest  # Ensure this exists

router = APIRouter(prefix="/public/partner-forms", tags=["PartnerFormPublic"])

@router.post("/{partner_id}/login", response_model=PartnerFormOut)
def partner_login(partner_id: str, creds: PartnerLoginRequest, db: Session = Depends(get_db)):
    """
    Authenticates a partner before allowing access to a form.
    """
    try:
        pf = PublicPartnerService.authenticate_partner(
            db, partner_id, creds.email, creds.password
        )
        return pf
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{partner_id}/answers", response_model=dict)
def submit_partner_answers(partner_id: str, data: PartnerFormAnswerCreate, db: Session = Depends(get_db)):
    """
    Saves form responses submitted by a partner.
    """
    try:
        new_answers = PublicPartnerService.save_answers(db, partner_id, data.answers)
        return {"message": "Answers submitted successfully", "id": new_answers.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
