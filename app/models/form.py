# app/models/form.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    published = Column(Boolean, default=False)

    sections = relationship("Section", back_populates="form", cascade="all, delete-orphan")
