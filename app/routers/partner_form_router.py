from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.partner_form_service import PartnerFormService
from app.schemas.partner_form_schema import PartnerFormCreate, PartnerFormUpdate, PartnerFormOut
from typing import List

router = APIRouter(prefix="/forms/{form_id}/participants", tags=["PartnerForm"])

@router.get("/", response_model=List[PartnerFormOut])
def list_participants_for_form(form_id: int, db: Session = Depends(get_db)):
    """
    List all participants for a form.
    """
    return PartnerFormService.list_for_form(db, form_id)

@router.post("/", response_model=PartnerFormOut)
def create_participant_for_form(form_id: int, data: PartnerFormCreate, db: Session = Depends(get_db)):
    """
    Create a new participant with auto-generated credentials.
    """
    try:
        return PartnerFormService.create_partner_form(db, form_id, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{pf_id}/regenerate-password", response_model=PartnerFormOut)
def regenerate_password(form_id: int, pf_id: int, db: Session = Depends(get_db)):
    """
    Regenerates a new password for a participant.
    """
    try:
        return PartnerFormService.regenerate_password(db, pf_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
