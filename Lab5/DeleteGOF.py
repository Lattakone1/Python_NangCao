import mysql.connector

# Connect to MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="121002",
        database="guidb"
    )

# Method to show data (already created)
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

# Method to delete a record
def deleteRecord():
    conn = connect()
    cursor = conn.cursor()

    # Execute DELETE command to remove the book with Book_ID = 1
    cursor.execute("DELETE FROM books WHERE Book_ID = 1")

    # Commit the changes to the database
    conn.commit()

    # Confirm deletion by showing the updated data
    showData()

    cursor.close()
    conn.close()

# Call methods
deleteRecord()  # This will delete the record and then show the updated data
