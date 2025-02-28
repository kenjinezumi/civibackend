# app/models/page.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    form = relationship("Form", back_populates="pages")

    sections = relationship(
        "Section",
        back_populates="page",
        cascade="all, delete-orphan"
    )

    # If you want "unsectioned" in DB, add something like:
    # unsectioned = relationship(
    #     "Question",
    #     back_populates="page_unsectioned",
    #     cascade="all, delete-orphan"
    # )
