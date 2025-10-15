from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserLogin(BaseModel):
    username: str
    password: str

class CaseCreate(BaseModel):
    case_id: str
    bank_code: str
    borrower_name: str
    loan_amount: float
    due_amount: float
    days_past_due: int
    priority: str
    region: str

class CaseResponse(CaseCreate):
    id: int
    assigned_team: str
    status: str
    class Config:
        orm_mode = True
