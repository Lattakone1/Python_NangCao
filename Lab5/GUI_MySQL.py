import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to MySQL (adjust with your own database details)
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="121002",
            database="ten_lattakone"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None

# Create GUI window
root = tk.Tk()
root.title("Python GUI")
root.geometry("500x400")

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a sample application"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Notebook (Tabs)
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="MySQL")
notebook.add(tab2, text="Widgets")
notebook.pack(expand=True, fill='both')

# Frame 1 - Python Database
frame_db = ttk.Labelframe(tab1, text="Python Database")
frame_db.pack(pady=10, padx=10, fill="both")

# Book title and page fields (3 separate text boxes for each)
lbl_title = ttk.Label(frame_db, text="Book Title:")
lbl_title.grid(row=0, column=0, padx=5, pady=5)

txt_title1 = ttk.Entry(frame_db)
txt_title1.grid(row=1, column=0, padx=5, pady=5)

txt_title2 = ttk.Entry(frame_db)
txt_title2.grid(row=2, column=0, padx=5, pady=5)

txt_title3 = ttk.Entry(frame_db)
txt_title3.grid(row=3, column=0, padx=5, pady=5)

lbl_page = ttk.Label(frame_db, text="Page:")
lbl_page.grid(row=0, column=2, padx=5, pady=5)

txt_page1 = ttk.Entry(frame_db)
txt_page1.grid(row=1, column=2, padx=5, pady=5)

txt_page2 = ttk.Entry(frame_db)
txt_page2.grid(row=2, column=2, padx=5, pady=5)

txt_page3 = ttk.Entry(frame_db)
txt_page3.grid(row=3, column=2, padx=5, pady=5)

# Buttons
btn_insert = ttk.Button(frame_db, text="Insert Quote")
btn_insert.grid(row=1, column=3, padx=5, pady=5)

btn_get = ttk.Button(frame_db, text="Get Quotes")
btn_get.grid(row=2, column=3, padx=5, pady=5)

btn_modify = ttk.Button(frame_db, text="Modify Quote")
btn_modify.grid(row=3, column=3, padx=5, pady=5)

# Frame 2 - Book Quotation
frame_quotation = ttk.Labelframe(tab1, text="Book Quotation")
frame_quotation.pack(pady=10, padx=10, fill="both")

txt_output = tk.Text(frame_quotation, height=10)
txt_output.pack(padx=5, pady=5)

# Insert quote function with input validation
# Insert quote function with input validation
def insert_quote():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO quotes (book_title, page) VALUES (%s, %s)"

        # Validate if the fields are not empty
        inserted_titles = []
        if txt_title1.get() and txt_page1.get():
            cursor.execute(query, (txt_title1.get(), txt_page1.get()))
            inserted_titles.append(f"Title: {txt_title1.get()}, Page: {txt_page1.get()}")
        if txt_title2.get() and txt_page2.get():
            cursor.execute(query, (txt_title2.get(), txt_page2.get()))
            inserted_titles.append(f"Title: {txt_title2.get()}, Page: {txt_page2.get()}")
        if txt_title3.get() and txt_page3.get():
            cursor.execute(query, (txt_title3.get(), txt_page3.get()))
            inserted_titles.append(f"Title: {txt_title3.get()}, Page: {txt_page3.get()}")

        connection.commit()
        connection.close()

        # Clear the text box and show inserted quotes
        txt_output.delete('1.0', tk.END)
        if inserted_titles:
            txt_output.insert(tk.END, "Inserted Quotes:\n" + "\n".join(inserted_titles))
        else:
            txt_output.insert(tk.END, "No quotes inserted.")
    else:
        messagebox.showerror("Error", "Failed to connect to the database.")

# Function to retrieve and display quotes
def get_quotes():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quotes WHERE book_title=%s", (txt_title1.get(),))
        rows = cursor.fetchall()

        # Clear the text box and display the retrieved quotes
        txt_output.delete('1.0', tk.END)
        if rows:
            txt_output.insert(tk.END, "Retrieved Quotes:\n")
            for row in rows:
                txt_output.insert(tk.END, f"Title: {row[1]}, Page: {row[2]}\n")
        else:
            txt_output.insert(tk.END, "No quotes found for the given book title.")
        connection.close()

# Function to modify an existing quote
def modify_quote():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE quotes SET page=%s WHERE book_title=%s AND page=%s"

        modified_titles = []
        # Modify each quote with its corresponding title and page number
        if txt_title1.get() and txt_page1.get():
            cursor.execute(query, (txt_page1.get(), txt_title1.get(), txt_page1.get()))
            modified_titles.append(f"Modified: Title: {txt_title1.get()}, Page: {txt_page1.get()}")
        if txt_title2.get() and txt_page2.get():
            cursor.execute(query, (txt_page2.get(), txt_title2.get(), txt_page2.get()))
            modified_titles.append(f"Modified: Title: {txt_title2.get()}, Page: {txt_page2.get()}")
        if txt_title3.get() and txt_page3.get():
            cursor.execute(query, (txt_page3.get(), txt_title3.get(), txt_page3.get()))

        connection.commit()
        connection.close()

        # Clear the text box and show modified quotes
        txt_output.delete('1.0', tk.END)
        if modified_titles:
            txt_output.insert(tk.END, "Modified Quotes:\n" + "\n".join(modified_titles))
        else:
            txt_output.insert(tk.END, "No quotes modified.")

# Assign button commands
btn_insert.config(command=insert_quote)
btn_get.config(command=get_quotes)
btn_modify.config(command=modify_quote)

root.mainloop()
