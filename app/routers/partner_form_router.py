# app/routers/partner_form_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4

from app.schemas.partner_form_schema import (
    PartnerFormCreate,
    PartnerFormOut,
    PartnerFormUpdate
)
from app.services.partner_form_service import PartnerFormService
from app.db.session import get_db

router = APIRouter(prefix="/forms/{form_id}/participants", tags=["PartnerForm"])

@router.get("/", response_model=List[PartnerFormOut])
def list_participants_for_form(form_id: int, db: Session = Depends(get_db)):
    """List all participant records (PartnerForms) for a specific Form."""
    return PartnerFormService.list_for_form(db, form_id)

@router.post("/", response_model=PartnerFormOut)
def create_participant_for_form(
    form_id: int,
    data: PartnerFormCreate,
    db: Session = Depends(get_db)
):
    """Create a new participant under a specific form_id."""
    try:
        pf = PartnerFormService.create_partner_form(db, form_id, data)
        return pf
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{pf_id}", response_model=PartnerFormOut)
def update_participant_for_form(
    form_id: int,
    pf_id: int,
    updates: PartnerFormUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing participant's record (name, email, password, completion...)."""
    try:
        pf = PartnerFormService.update_partner_form(db, pf_id, updates)
        if pf.form_id != form_id:
            raise ValueError("Participant does not belong to this form.")
        return pf
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{pf_id}")
def delete_participant_for_form(
    form_id: int,
    pf_id: int,
    db: Session = Depends(get_db)
):
    """Remove an existing participant from the given form."""
    try:
        # Possibly verify the record belongs to that form
        pf_obj = PartnerFormService.update_partner_form(db, pf_id, PartnerFormUpdate())
        if pf_obj.form_id != form_id:
            raise ValueError("Participant not part of this form.")
        # Actually remove it
        PartnerFormService.delete_partner_form(db, pf_id)
        return {"message": "Participant removed."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{pf_id}/regenerate-password", response_model=PartnerFormOut)
def regenerate_password_for_form(
    form_id: int,
    pf_id: int,
    db: Session = Depends(get_db)
):
    """
    Regenerate this participant's password.
    Endpoint: POST /forms/{form_id}/participants/{pf_id}/regenerate-password
    """
    # 1) Fetch the participant
    pf_obj = PartnerFormService.get_partner_form_by_id(db, pf_id)
    if not pf_obj:
        raise HTTPException(status_code=404, detail="Participant not found")

    # 2) Ensure the participant belongs to the correct form
    if pf_obj.form_id != form_id:
        raise HTTPException(status_code=404, detail="Participant not part of this form.")

    # 3) Generate a new random password (simple example)
    new_password = str(uuid4())[:8]

    # 4) Update in DB
    pf_obj = PartnerFormService.update_partner_form(
        db=db,
        pf_id=pf_id,
        updates=PartnerFormUpdate(password=new_password)
    )
    return pf_obj