import psycopg2

connection = psycopg2.connect(
    database="test",
    user="postgres",
    password="SergejShake4.0",
    host="localhost"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM person")

for row in cursor:
    print(row)