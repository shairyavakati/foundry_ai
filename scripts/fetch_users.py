import psycopg2
from scripts.db_connection import get_connection

def view_users():
    connection = None
    cursor = None
    try:
    
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        for user in users:
            print("User ID :", user[0])
            print("Name    :", user[1])
            print("Email   :", user[2])
            print("Mobile  :", user[3])
            print("----------------------------")
    except Exception as e:
        print("❌ Database Error:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
