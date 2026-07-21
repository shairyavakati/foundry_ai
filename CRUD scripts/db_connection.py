import psycopg2
def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="foundry_ai",
            user="postgres",
            password="Daddy@13",
            port="5432"
        )
        return connection
    except Exception as e:
        print("❌ Connection Failed!")
        print(e)
        return None
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