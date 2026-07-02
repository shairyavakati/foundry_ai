import psycopg2
from scripts.db_connection import get_connection
def update_user():
    User_ID = input("Enter User ID to update: ")
    email = input("Enter new Email: ")
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE users SET email = %s WHERE user_id = %s;",
            (email, User_ID)
        )
        connection.commit()
        print("✅ User Updated Successfully!")
    except Exception as e:
        print("❌ Database Error:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        
    
