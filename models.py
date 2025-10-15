from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum

class Role(str, enum.Enum):
    admin = "Admin"
    lead = "TeamLead"
    agent = "Agent"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(Role), default=Role.agent)

class CaseStatus(str, enum.Enum):
    pending = "Pending"
    in_progress = "In Progress"
    resolved = "Resolved"
    escalated = "Escalated"

class Case(Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(String, unique=True, index=True)
    bank_code = Column(String)
    borrower_name = Column(String)
    loan_amount = Column(Float)
    due_amount = Column(Float)
    days_past_due = Column(Integer)
    priority = Column(String)
    region = Column(String)
    assigned_team = Column(String)
    status = Column(Enum(CaseStatus), default=CaseStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class AuditTrail(Base):
    __tablename__ = "audit_trail"
    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(String)
    old_status = Column(String)
    new_status = Column(String)
    changed_at = Column(DateTime, default=datetime.utcnow)
