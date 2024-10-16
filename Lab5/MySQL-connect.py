import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    user='root',       # Your MySQL username (default is 'root')
    password='121002',  # Your MySQL password
    host='127.0.0.1',  # Localhost
    database='ten_lattakone'  # Your database name
)

if conn.is_connected():
    print("Connected to MySQL Database")

conn.close()
