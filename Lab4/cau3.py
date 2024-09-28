import tkinter as tk

# Global Variables (module-level)
global_var1 = "Hello from Global Variable"
global_var2 = 100

# Constants (by convention, constants are written in uppercase)
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458  # in meters per second

# Function to access global variables and constants
def show_globals():
    # Access global variables and constants within the Tkinter window
    text_area.insert(tk.INSERT, f"Global Variable 1: {global_var1}\n")
    text_area.insert(tk.INSERT, f"Global Variable 2: {global_var2}\n")
    text_area.insert(tk.INSERT, f"PI Constant: {PI}\n")
    text_area.insert(tk.INSERT, f"Gravity Constant: {GRAVITY}\n")
    text_area.insert(tk.INSERT, f"Speed of Light Constant: {SPEED_OF_LIGHT}\n")

# Tkinter GUI setup
root = tk.Tk()
root.title("Global Variables and Constants Example")

# Create a Text widget to display information
text_area = tk.Text(root, width=50, height=10)
text_area.pack()

# Button to trigger the display of global variables and constants
btn_show = tk.Button(root, text="Show Globals and Constants", command=show_globals)
btn_show.pack()

# Run the Tkinter event loop
root.mainloop()
