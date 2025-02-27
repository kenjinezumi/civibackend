# app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# from app.models.form import Form
from app.models.section import Section
from app.models.question import Question
from app.models.partner_form import PartnerForm