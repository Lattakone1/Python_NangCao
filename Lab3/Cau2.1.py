import tkinter as tk
from tkinter import messagebox

# Create the main window (root)
root = tk.Tk()
root.title("Tk")
root.geometry("300x200")

# Create a button to show the messagebox
def show_message():
    messagebox.showinfo("Python Message Info Box", "Python GUI created using tkinter:The year is 2022")

# Add button to the window
button = tk.Button(root, text="Show", command=show_message)
button.pack(pady=20)

# Run the application
root.mainloop()

