from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from  env_secrets import *

DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/Bank_managementdb"

try:
    engine=create_engine(DATABASE_URL)
    conn = engine.connect()
    print("Database Connected Successfully")
except Exception as e:
    print("Database Connection Failed")
    print(e)

Base = declarative_base()