# app/schemas/form_schema.py
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Union
from datetime import datetime

#
# Skip Logic
#
class SkipLogicCondition(BaseModel):
    referenceQuestionIndex: int
    operator: str  # e.g. '==', '!=', 'contains', etc.
    value: str     # the value to compare
    targetSectionId: Optional[int] = None
    targetQuestionId: Optional[int] = None
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
    skipLogic: Optional[SkipLogicCondition] = Field(None, alias="skip_logic")
    ratingMin: Optional[int] = None
    ratingMax: Optional[int] = None

class QuestionOut(BaseModel):
    id: int
    label: str
    type: str
    required: bool
    placeholder: str
    helpText: str
    choices: List[str] = []
    ratingMin: Optional[int] = None
    ratingMax: Optional[int] = None

    skipLogic: Optional[SkipLogicCondition] = Field(None, alias="skip_logic")

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
    due_date: Optional[datetime] = None

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
    due_date: Optional[Union[datetime, str]] = None  # Accepts both datetime & str

    @validator("due_date", pre=True, always=True)
    def parse_due_date(cls, value):
        if value in (None, "", "null"):  # Handle empty string & 'null' string
            return None  # Convert to NULL for DB
        try:
            return datetime.fromisoformat(value)  # Ensure proper datetime format
        except ValueError:
            raise ValueError("Invalid datetime format. Expected ISO format (YYYY-MM-DD).")
        
class FormOut(FormBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    pages: List[PageOut] = []

    class Config:
        orm_mode = True
