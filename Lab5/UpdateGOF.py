import mysql.connector
# Connect to MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="121002",
        database="guidb"
    )
# Method to show data
def showData():
    conn = connect()
    cursor = conn.cursor()
    # Execute SELECT statement for books
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("Books: ", books)

    # Execute SELECT statement for quotations
    cursor.execute("SELECT * FROM quotations")
    quotations = cursor.fetchall()
    print("Quotations: ", quotations)

    cursor.close()
    conn.close()

# Method to update data
def updateGOF():
    conn = connect()
    cursor = conn.cursor()

    # Execute the UPDATE command
    cursor.execute("""
        UPDATE quotations
        SET Quotation = 'Pythonic Duck Typing: If it walks like a duck and talks like a duck it probably is a duck...'
        WHERE Books_Book_ID = 1
    """)
    # Commit the changes
    conn.commit()

    # Fetch and show updated data
    cursor.execute("SELECT Book_ID FROM books WHERE Book_Title = 'Design Patterns'")
    primKey = cursor.fetchone()[0]
    print("Primary key: ", primKey)

    cursor.execute("SELECT * FROM quotations WHERE Books_Book_ID = (%s)", (primKey,))
    print(cursor.fetchall())

    cursor.close()
    conn.close()

# Call methods
updateGOF()
showData()
