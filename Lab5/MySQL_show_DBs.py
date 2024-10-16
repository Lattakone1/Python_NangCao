# MySQL_show_DBs.py

import mysql.connector
import GuiDBConfig as guiConf  # Import the configuration module

# Unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")  # Execute the SQL command to show databases
print(cursor.fetchall())  # Print the list of databases
conn.close()