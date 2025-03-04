# app/models/partner_form.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class PartnerForm(Base):
    __tablename__ = "partner_forms"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    form = relationship("Form", back_populates="published_forms")

    # We store a unique partner_id or "slug"
    partner_id = Column(String, nullable=False, unique=True)
    partner_name = Column(String, nullable=True)
    partner_email = Column(String, nullable=True)

    # NEW: store a password or hashed password
    password = Column(String, nullable=True)

    completion_percentage = Column(Float, default=0.0)
    answer_record = relationship("PartnerFormAnswer", uselist=False, back_populates="partner_form")
