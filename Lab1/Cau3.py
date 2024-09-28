import tkinter as tk
from tkinter import ttk

#Create win
win = tk.Tk()

#Add a title
win.title("Python GUI")

#Adding a label
ttk.Label(win,text="A label").grid(column=0,row=0)

#Start GUI
win.mainloop()