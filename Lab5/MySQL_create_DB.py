import mysql.connector
from mysql.connector import errorcode
# Connection information
config = {
    'user': 'root',  # replace with your MySQL username
    'password': '121002',  # replace with your MySQL password
    'host': '127.0.0.1'  # replace with your MySQL host
}
# Connect to MySQL server
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    # Check if database exists, if not create it
    cursor.execute("CREATE DATABASE IF NOT EXISTS guidb")
    print("Database 'guidb' is ready to use.")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        print("Database already exists.")
    else:
        print(f"Failed to create database: {err}")
finally:
    # Close the connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()

