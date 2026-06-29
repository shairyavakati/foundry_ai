import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="foundry_ai",
        user="postgres",
        password="Daddy@13",
        port="5432"
    )

    print("✅ Connected to PostgreSQL Successfully!")

    connection.close()
    print("🔌 Connection Closed.")

except Exception as e:
    print("❌ Connection Failed!")
    print(e)