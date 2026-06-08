from sqlalchemy import text
from database import engine

with engine.connect() as conn:
    conn.execute(text("CREATE SCHEMA bank"))
    conn.commit()

print("Schema created successfully!")