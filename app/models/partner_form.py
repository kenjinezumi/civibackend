from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class PartnerForm(Base):
    __tablename__ = "partner_forms"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)

    partner_id = Column(String, nullable=False)
    partner_name = Column(String, nullable=True)
    partner_email = Column(String, nullable=True)

    public_url = Column(String, unique=True, nullable=False)
    completion_percentage = Column(Float, default=0.0)

    form = relationship("Form", back_populates="published_forms")
