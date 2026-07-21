import psycopg2
from scripts.db_connection import get_connection
from validations.validation_engine import get_valid_input


def add_user():
    name = get_valid_input(
        "Enter Name: ",
        2,
        50,
        "Name cannot be empty.",
        "Name must contain at least 2 characters."
    )
    email = get_valid_input(
        "Enter Email: ",
        5,
        100,
        "Email cannot be empty.",
        "Email must contain at least 5 characters."
    )
    email = get_valid_input(
        "Enter Email: ",
        5,
        100,
        "Email cannot be empty.",
        "Email must contain at least 5 characters."
    )
    mobile = get_valid_input(
        "Enter Mobile Number: ",
        10,
        10,
        "Mobile Number cannot be empty.",
        "Mobile Number must contain at least 10 characters."
    )
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
        print(" User Added Successfully!")
    
    
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
