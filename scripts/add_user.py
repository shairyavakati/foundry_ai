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
    
    
        def add_user():
            
            print("1. Inputs received")

        connection = get_connection()
        print("2. Connected")

        cursor = connection.cursor()
        print("3. Cursor created")

        cursor.execute(
            "INSERT INTO users(name, email, mobile_no) VALUES (%s, %s, %s)",
            (name, email, mobile)
        )

        print("4. Query executed")

        connection.commit()
        print("5. Commit successful")
   
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
