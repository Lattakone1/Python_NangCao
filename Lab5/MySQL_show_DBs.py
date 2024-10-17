import mysql.connector
import GuiDBConfig as guiConf

# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

print(cursor.fetchall())
conn.close()

