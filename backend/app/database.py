import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="Bank_managementdb",
        user="postgres",
        password="postgres"
    )

    print("Database connection successful!")

    cur = conn.cursor()

    cur.execute("CREATE SCHEMA IF NOT EXISTS bank")

    cur.execute("""
    CREATE TABLE bank.accounts(
        account_id SERIAL PRIMARY KEY,
        account_number VARCHAR(20) UNIQUE,
        account_holder_name VARCHAR(100),
        account_type VARCHAR(20),
        balance NUMERIC(12,2),
        created_at TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE bank.transactions(
        transaction_id SERIAL PRIMARY KEY,
        account_id INTEGER,
        transaction_type VARCHAR(20),
        amount NUMERIC(12,2)
    )
    """)

    cur.execute("""
    CREATE TABLE bank.system_logs(
        log_id SERIAL PRIMARY KEY,
        action VARCHAR(100),
        status VARCHAR(20),
        log_time TIMESTAMP,
        details TEXT
    )
    """) 
              
    conn.commit()

    print("Schema and table created successfully!")

    cur.close()
    conn.close()


except Exception as e:
    print("Database connection failed!")
    print(e)