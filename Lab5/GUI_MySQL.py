import mysql.connector as mysql

class MySQLConnector:
    def __init__(self, config):
        """Initialize with database configuration dictionary."""
        self.config = config
        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to the MySQL database using the provided configuration."""
        try:
            self.conn = mysql.connect(**self.config)
            self.cursor = self.conn.cursor()
            print("Connection successful")
        except mysql.Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None
            self.cursor = None
    
    def use_database(self, db_name):
        """Switch to the specified database."""
        if self.cursor is None:
            print("Cursor is not initialized. Cannot execute query.")
            return

        try:
            self.cursor.execute(f"USE {db_name}")
            print(f"Using database: {db_name}")
        except mysql.Error as e:
            print(f"Error using database: {e}")
    
    def create_table(self):
        """Create a table in the connected database."""
        if self.cursor is None:
            print("Cursor is not initialized. Cannot create table.")
            return

        create_table_query = """
        CREATE TABLE IF NOT EXISTS Books (
            Book_ID INT NOT NULL AUTO_INCREMENT,
            Book_Title VARCHAR(25) NOT NULL,
            Book_Page INT NOT NULL,
            PRIMARY KEY (Book_ID)
        ) ENGINE=InnoDB
        """
        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()  # Commit the transaction
            print("Table 'Books' created successfully")
        except mysql.Error as e:
            print(f"Error creating table: {e}")

    def close(self):
        """Close the connection to the MySQL database."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Connection closed")


# Example of usage:

if __name__ == "__main__":
    # Define credentials directly in the script
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '121002',
        'database': 'ten_lattakone'
    }

    # Create an instance of MySQLConnector
    db = MySQLConnector(db_config)

    # Connect to the database
    db.connect()

    # Ensure the connection was successful before proceeding
    if db.conn and db.cursor:
        # Select the 'guidb' database
        db.use_database("guidb")

        # Create the 'Books' table
        db.create_table()

    # Close the connection
    db.close()
