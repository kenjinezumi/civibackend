# app/schemas/answer_schema.py

from pydantic import BaseModel
from typing import Dict, Any

class PartnerFormAnswerCreate(BaseModel):
    partner_form_id: int  # ID linking to the PartnerForm
    answers_data: Dict[str, Any]  # Stores all answers in a flexible format

    class Config:
        orm_mode = True
