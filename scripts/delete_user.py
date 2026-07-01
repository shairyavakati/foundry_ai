import psycopg2
from scripts.db_connection import get_connection

def delete_user():
    User_ID = input("Enter User ID to delete: ")

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE user_id = %s;",
            (User_ID,)
        )
        user = cursor.fetchone()
        if user is None:
            print("❌ User not found!")
            return

        cursor.execute(
            "DELETE FROM users WHERE user_id = %s;",
            (User_ID,)
        )
        connection.commit()
        print("✅ User Deleted Successfully!")
    except Exception as e:
        print("❌ Database Error:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        # No further commit here; commits are handled after successful operations.

