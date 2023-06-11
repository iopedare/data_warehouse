from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
pgpassword = os.environ.get('POSTGRES_PASSWORD')
conn = None
try:
    conn = psycopg2.connect(
        user = "postgres",
        password = pgpassword,
        host = "localhost",
        port = "5432",
        database = "postgres"
    )
except Exception as e:
    print("Error connectiong to data warehouse")
    print(e)
else:
    print("Successfully connected to data warehouse")
finally:
    if conn:
        conn.close()
        print("Connection Closed")
