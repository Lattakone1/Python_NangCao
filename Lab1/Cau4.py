import tkinter as tk
from tkinter import ttk

win = tk.Tk()

#adding a Label that will get modified
a_label = ttk.Label(win, text="ALabel")
a_label.grid(column=0, row=0)

#Button Click Event Fuction
def click_me():
    action.configure(text="** I have been Clicked **")
    a_label.configure(foreground="red")
    a_label.configure(text="A Red label")
#Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1,row=0)

#Start GUI
win.mainloop()