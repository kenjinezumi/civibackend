# app/models/question.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    type = Column(String, default="text")  # 'radio', 'select', etc.
    required = Column(Boolean, default=False)

    placeholder = Column(String, default="")
    helpText = Column(String, default="")
    ratingMin = Column(Integer, nullable=True)
    ratingMax = Column(Integer, nullable=True)

    # For multiple choice
    choices = Column(JSONB, default=[])  # store array of strings

    skip_logic = Column(JSONB, nullable=True)  # e.g. skipLogic

    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    section = relationship("Section", back_populates="questions")
