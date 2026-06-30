import psycopg2
def update_user():
    User_ID = input("Enter User ID to update: ")
    email = input("Enter new Email: ")
    connection = psycopg2.connect(
        host="localhost",
        database="foundry_ai",
        user="postgres",
        password="Daddy@13",
        port="5432"
    )
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET email = %s WHERE user_id = %s;",
        (email, User_ID)
    )
    print("✅ User Updated Successfully!")
    connection.commit()
    cursor.close()
    connection.close()
