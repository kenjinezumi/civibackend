from pydantic import BaseModel

class PartnerLoginRequest(BaseModel):
    email: str
    password: str
