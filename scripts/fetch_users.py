import psycopg2
connection = psycopg2.connect(
        host="localhost",
        database="foundry_ai",
        user="postgres",
        password="Daddy@13",
        port="5432"
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
users = cursor.fetchmany(3)
print(users)

cursor.close()