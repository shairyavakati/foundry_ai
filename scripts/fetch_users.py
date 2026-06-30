import psycopg2
def view_users():
    connection = psycopg2.connect(
        host="localhost",
        database="foundry_ai",
        user="postgres",
        password="Daddy@13",
        port="5432"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    for user in users:
        print("User ID :", user[0])
        print("Name    :", user[1])
        print("Email   :", user[2])
        print("Mobile  :", user[3])
        print("----------------------------")

    cursor.close()
    connection.close()
