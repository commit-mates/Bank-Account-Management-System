from fastapi import FastAPI

from database import engine, Base

from models.account import Account
from models.transaction import Transaction
from models.system_log import SystemLog

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"FastAPI is running"}