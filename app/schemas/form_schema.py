# app/schemas/form_schema.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#
# Skip Logic
#
class SkipLogicCondition(BaseModel):
    referenceQuestionIndex: int
    operator: str
    value: str
    action: str

#
# QUESTION
#
class QuestionCreate(BaseModel):
    label: str
    type: str = "text"      # e.g. 'radio', 'rating'
    required: bool = False
    placeholder: str = ""
    helpText: str = ""
    choices: List[str] = []
    skipLogic: Optional[SkipLogicCondition] = None
    # ratingMin: Optional[int] = None
    # ratingMax: Optional[int] = None

class QuestionOut(BaseModel):
    id: int
    label: str
    type: str
    required: bool
    placeholder: str
    helpText: str
    choices: List[str]
    skipLogic: Optional[SkipLogicCondition] = None

    class Config:
        orm_mode = True

#
# SECTION
#
class SectionCreate(BaseModel):
    title: str
    questions: List[QuestionCreate] = []

class SectionOut(BaseModel):
    id: int
    title: str
    questions: List[QuestionOut] = []

    class Config:
        orm_mode = True

#
# PAGE
#
class PageCreate(BaseModel):
    title: str
    description: Optional[str] = None
    # If you want unsectioned:
    unsectioned: List[QuestionCreate] = []
    sections: List[SectionCreate] = []

class PageOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    unsectioned: List[QuestionOut] = []
    sections: List[SectionOut] = []

    class Config:
        orm_mode = True

#
# FORM
#
class FormBase(BaseModel):
    title: str
    description: Optional[str] = None
    published: bool = False
    country: Optional[str] = None
    created_by: Optional[str] = None

class FormCreate(FormBase):
    title: str
    description: str
    published: bool
    country: str
    created_by: str
    pages: List[PageCreate] = []

class FormUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    published: Optional[bool]
    country: Optional[str]
    created_by: Optional[str]
    pages: Optional[List[PageCreate]]

class FormOut(FormBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    pages: List[PageOut] = []

    class Config:
        orm_mode = True
