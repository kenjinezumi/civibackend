from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.partner_form_schema import PartnerFormCreate, PartnerFormOut
from app.services.partner_form_service import PartnerFormService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/partner-forms", tags=["partner-forms"])

@router.post("/", response_model=PartnerFormOut)
def create_partner_form(data: PartnerFormCreate, db: Session = Depends(get_db)):
    try:
        return PartnerFormService.create_partner_form(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/slug/{slug}", response_model=PartnerFormOut)
def get_by_slug(slug: str, db: Session = Depends(get_db)):
    pf = PartnerFormService.get_by_slug(db, slug)
    if not pf:
        raise HTTPException(status_code=404, detail="Not found")
    return pf

@router.put("/slug/{slug}/completion", response_model=PartnerFormOut)
def update_completion(slug: str, new_completion: float, db: Session = Depends(get_db)):
    try:
        return PartnerFormService.update_completion(db, slug, new_completion)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
