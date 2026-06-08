from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from database import Base

class Account(Base):
    __tablename__ = "accounts"
    __table_args__ = {"schema": "bank"}

    account_id = Column(Integer, primary_key=True)
    account_number = Column(String(20), unique=True)
    account_holder_name = Column(String(100))
    account_type = Column(String(20))
    balance = Column(Numeric(12,2))
    created_at = Column(TIMESTAMP)