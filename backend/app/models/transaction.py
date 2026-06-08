from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    __table_args__ = {"schema": "bank"}

    transaction_id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    transaction_type = Column(String(20))
    amount = Column(Numeric(12,2))
    transaction_time = Column(TIMESTAMP)
    status = Column(String(20))