from database import engine, Base

from models.account import Account
from models.transaction import Transaction
from models.system_log import SystemLog

Base.metadata.create_all(bind=engine)

print("All tables created successfully!")