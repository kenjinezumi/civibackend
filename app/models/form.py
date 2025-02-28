# app/models/form.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    published = Column(Boolean, default=False)
    country = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(String, nullable=True)

    # Instead of sections = ...
    # We now have pages relationship
    pages = relationship(
        "Page",
        back_populates="form",
        cascade="all, delete-orphan"
    )

    # partner forms
    published_forms = relationship("PartnerForm", back_populates="form", cascade="all, delete-orphan")
