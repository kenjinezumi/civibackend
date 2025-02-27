# app/schemas/form_schema.py
from pydantic import BaseModel
from datetime import datetime

from typing import List, Optional

class QuestionBase(BaseModel):
    label: str
    type: str = "text"
    required: bool = False

class QuestionCreate(QuestionBase):
    pass

class QuestionOut(QuestionBase):
    id: int

    class Config:
        orm_mode = True

class SectionBase(BaseModel):
    title: str

class SectionCreate(SectionBase):
    questions: List[QuestionCreate] = []

class SectionOut(SectionBase):
    id: int
    questions: List[QuestionOut] = []

    class Config:
        orm_mode = True

class FormBase(BaseModel):
    title: str
    description: Optional[str] = None
    published: bool = False
    country: Optional[str] = None
    created_by: Optional[str] = None

class FormCreate(FormBase):
    sections: List[SectionCreate] = []

class FormUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    published: Optional[bool]
    country: Optional[str]
    created_by: Optional[str]

class FormOut(FormBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    sections: List[SectionOut] = []

    class Config:
        orm_mode = True
