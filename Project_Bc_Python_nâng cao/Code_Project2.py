import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox

# Database connection
def connect_db(dbname='postgres'):
    try:
        conn = psycopg2.connect(
            dbname="Lattakone",
            user="postgres",
            password="1234",
            host="localhost",
            port='5432'
        )
        print(f"Connection to {dbname} successful")
        return conn
    except Exception as e:
        print(f"Error while connecting to database {dbname}:", e)
        raise

def create_database():
    try:
        conn = connect_db()
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE books")
        cur.close()
        conn.close()
        print("Database 'books' created successfully")
    except psycopg2.errors.DuplicateDatabase:
        print("Database 'books' already exists")
    except Exception as e:
        print("Error creating database:", e)
        raise

def create_table(connection):
    if connection is None:
        messagebox.showerror("Database Error", "Unable to connect to the database")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                year INTEGER NOT NULL,
                genre VARCHAR(100) NOT NULL
            );
        """)
        connection.commit()
        print("Table 'books' has been created successfully.")
    except Exception as e:
        print("Error while creating table:", e)
        messagebox.showerror("Database Error", str(e))
    finally:
        if cursor:
            cursor.close()

# Add book to the database
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    genre = entry_genre.get()

    if not validate_input(title, author, year, genre):
        return

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s)",
                    (title, author, int(year), genre))
        conn.commit()
        cur.close()
        conn.close()
        reload_books()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Update selected book
def update_book():
    try:
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a book to update.")
            return

        book_id = tree.item(selected_item)['values'][0]
        title = entry_title.get()
        author = entry_author.get()
        year = entry_year.get()
        genre = entry_genre.get()

        if not validate_input(title, author, year, genre):
            return

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE books SET title=%s, author=%s, year=%s, genre=%s WHERE id=%s",
                    (title, author, int(year), genre, book_id))
        conn.commit()
        cur.close()
        conn.close()
        reload_books()
    except Exception as e:
        messagebox.showerror("Update Error", str(e))

# Delete selected book
def delete_book():
    try:
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a book to delete.")
            return

        book_id = tree.item(selected_item)['values'][0]

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
        conn.commit()
        cur.close()
        conn.close()
        reload_books()
    except Exception as e:
        messagebox.showerror("Delete Error", str(e))

# Reload the book list from database
def reload_books():
    try:
        conn = connect_db('books')
        cur = conn.cursor()
        
        # Kiểm tra xem bảng có tồn tại không
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'books'
            );
        """)
        table_exists = cur.fetchone()[0]
        
        if not table_exists:
            create_table(conn)
        
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        
        # Clear existing data
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Load Error", str(e))
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Validate input fields
def validate_input(title, author, year, genre):
    if not title or not author or not year or not genre:
        messagebox.showwarning("Input Error", "All fields are required.")
        return False
    try:
        int(year)
    except ValueError:
        messagebox.showwarning("Input Error", "Year must be a number.")
        return False
    return True

# Setup GUI
root = tk.Tk()
root.title("Library Management")

# Labels and entries
tk.Label(root, text="Book Title:").grid(row=0, column=0, padx=10, pady=5)
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Author:").grid(row=1, column=0, padx=10, pady=5)
entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Year XB:").grid(row=2, column=0, padx=10, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Category:").grid(row=3, column=0, padx=10, pady=5)
entry_genre = tk.Entry(root)
entry_genre.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add books", command=add_book).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Update information", command=update_book).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Delete book", command=delete_book).grid(row=4, column=2, padx=10, pady=10)
tk.Button(root, text="Reload list", command=reload_books).grid(row=4, column=3, padx=10, pady=10)

# Treeview for book list
columns = ("ID", "Book Title", "Author", "year XB", "Category")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Book Title", text="Book Title")
tree.heading("Author", text="Author")
tree.heading("year XB", text="year XB")
tree.heading("Category", text="Category")
tree.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

try:
    
    connection = connect_db('books')
    if connection:
        create_table(connection)
        connection.close()
except Exception as e:
    messagebox.showerror("Database Error", f"Unable to setup the database: {str(e)}")
    root.quit()

# Start with a load of books
reload_books()

# Run the application
root.mainloop()
