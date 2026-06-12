from database import engine, Base

from modules.accounts import Account
from modules.transactions import Transaction
from modules.system_logs import SystemLog

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")