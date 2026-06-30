import psycopg2
User_ID = input("Enter User ID to delete: ")
connection = psycopg2.connect(
        host="localhost",
        database="foundry_ai",
        user="postgres",
        password="Daddy@13",
        port="5432"
    )
cursor = connection.cursor()
cursor.execute(
    "DELETE FROM users WHERE user_id = %s;",
    (User_ID,)
)
print("✅ User Deleted Successfully!")
connection.commit()
cursor.close()
connection.close()