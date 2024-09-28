import tkinter as tk

# Create instance of tkinter
win = tk.Tk()

# Create StringVar
strData = tk.StringVar()

# Set the value to string type
strData.set('Hello StringVar')  # Set data

# Retrieve and print the value
varData = strData.get()
print(varData)  # Outputs: Hello StringVar
print(type(varData))  # Outputs: <class 'str'>
