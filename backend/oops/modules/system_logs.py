from sqlalchemy import Column, Integer, String, TIMESTAMP, Text
from database import Base

class SystemLog(Base):
    __tablename__ = "system_logs"
    __table_args__ = {"schema": "bank"}

    log_id = Column(Integer, primary_key=True)
    action = Column(String(100))
    status = Column(String(20))
    log_time = Column(TIMESTAMP)
    details = Column(Text)