import tkinter as tk

# Create instance of tkinter
win = tk.Tk()

# Create DoubleVar
doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.4)  # default value
print(type(doubleData))  # Outputs: <class 'float'>

add_doubles = 1.22222222222222222222222222222222222 + doubleData.get()
print(add_doubles)
print(type(add_doubles))



