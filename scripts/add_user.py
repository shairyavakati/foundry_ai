import psycopg2
Name = input("Enter Name   : ")
EMail = input("Enter Email  : ")
Mobile = input("Enter Phone number : ")
connection = psycopg2.connect(
        host="localhost",
        database="foundry_ai",
        user="postgres",
        password="Daddy@13",
        port="5432"
    )
cursor = connection.cursor()
cursor.execute(
    "INSERT INTO users(name, email, mobile_no ) VALUES (%s, %s, %s)",
    (Name, EMail, Mobile)
)
print("✅ User Added Successfully!")
connection.commit()
cursor.close()
connection.close()
