import psycopg2
from scripts.db_connection import get_connection


def add_user():
    name = input("Enter Name   : ")
    email = input("Enter Email  : ")
    mobile = input("Enter Phone number : ")
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users(name, email, mobile_no) VALUES (%s, %s, %s)",
            (name, email, mobile)
        )
        connection.commit()
        print("✅ User Added Successfully!")
    except Exception as e:
        # attempt rollback if possible
        if connection:
            try:
                connection.rollback()
            except Exception:
                pass
        print("❌ Database Error:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    add_user()
