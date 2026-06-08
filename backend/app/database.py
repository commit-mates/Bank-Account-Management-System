from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/Bank_managementdb"

engine = create_engine(DATABASE_URL)

Base = declarative_base()
