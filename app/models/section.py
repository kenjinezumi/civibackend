# app/models/section.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)

    form = relationship("Form", back_populates="sections")
    questions = relationship("Question", back_populates="section", cascade="all, delete-orphan")
