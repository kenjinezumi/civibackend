# app/models/partner_form_answer.py

from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base

class PartnerFormAnswer(Base):
    """
    Stores the entire submission from a partner for a given form in a JSON column.
    This way, we can store arbitrary question/answer structures.
    """
    __tablename__ = "partner_form_answers"

    id = Column(Integer, primary_key=True, index=True)

    # Link to the partner_form record (the participant)
    partner_form_id = Column(Integer, ForeignKey("partner_forms.id"), nullable=False)
    # You might have a partner_form relationship if you want:
    partner_form = relationship("PartnerForm", back_populates="answer_record")

    # The entire set of answers is stored here in JSON/dict form:
    # e.g. {
    #   "pages": [
    #     {
    #       "title": "Page 1",
    #       "sections": [
    #         {
    #           "title": "Section A",
    #           "questions": [
    #             { "label": "Q1", "type": "text", "value": "some user input" },
    #             ...
    #           ]
    #         }
    #       ]
    #     }
    #   ]
    # }
    answers_data = Column(JSON, nullable=False)
