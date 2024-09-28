import tkinter as tk
from tkinter import messagebox

# Create the main window (root)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Display the information message box
messagebox.showinfo("Python Message Info Box", "Python GUI created using tkinter: The year is 2022")

# Run the application
root.mainloop()