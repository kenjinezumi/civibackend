# app/schemas/partner_form_schema.py
from pydantic import BaseModel
from typing import Optional

class PartnerFormBase(BaseModel):
    partner_name: Optional[str] = None
    partner_email: Optional[str] = None
    password: Optional[str] = None
    completion_percentage: Optional[float] = None

class PartnerFormCreate(PartnerFormBase):
    """For creating a new participant (we do not require partner_id)."""
    # If you want them to optionally pass a password, you can. We'll auto-generate if not passed.
    pass

class PartnerFormUpdate(PartnerFormBase):
    """For partial updates: name, email, password, completion, etc."""
    pass

class PartnerFormOut(PartnerFormBase):
    """What we return to the client."""
    id: int
    partner_id: str
    form_id: int
    password: Optional[str] = None

    class Config:
        orm_mode = True
