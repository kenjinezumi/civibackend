# app/models/question.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    type = Column(String, default="text")
    required = Column(Boolean, default=False)

    placeholder = Column(String, default="")
    helpText = Column(String, default="")

    # If you want to store choices as JSON
    choices = Column(JSONB, nullable=True)

    # ratingMin / ratingMax if you want direct columns:
    # ratingMin = Column(Integer, nullable=True)
    # ratingMax = Column(Integer, nullable=True)

    # skip logic
    skip_logic = Column(JSONB, nullable=True)

    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    section = relationship("Section", back_populates="questions")

    # If you want unsectioned:
    # page_id = Column(Integer, ForeignKey("pages.id"), nullable=True)
    # page_unsectioned = relationship("Page", back_populates="unsectioned")
