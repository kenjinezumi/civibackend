# app/models/question.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=False)
    type = Column(String, default="text")
    required = Column(Boolean, default=False)

    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    section = relationship("Section", back_populates="questions")
