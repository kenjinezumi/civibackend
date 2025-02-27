from pydantic import BaseModel
from typing import Optional

class PartnerFormBase(BaseModel):
    partner_id: str
    partner_name: Optional[str] = None
    partner_email: Optional[str] = None
    public_url: str
    completion_percentage: float = 0.0

class PartnerFormCreate(PartnerFormBase):
    form_id: int

class PartnerFormOut(PartnerFormBase):
    id: int
    class Config:
        orm_mode = True
