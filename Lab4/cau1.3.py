import tkinter as tk

# Create the main window (optional if you're just testing variables)
root = tk.Tk()

# Create a StringVar and set an initial value
varData = tk.StringVar()
varData.set("Hello StringVar")

# Print the current value of strData
print(varData.get())

# Print out the default tkinter variable values
print(tk.IntVar())       # Default IntVar
print(tk.DoubleVar())    # Default DoubleVar
print(tk.BooleanVar())   # Default BooleanVar


