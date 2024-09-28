import tkinter as tk

root = tk.Tk()
root.title("Python GUI")

label = tk.Label(root, text="Mighty Python\nEnter a name:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(root)
entry.grid(row=1, column=0, sticky="ew")

checkbox = tk.Checkbutton(root, text="Disabled", state='disabled')
checkbox.grid(row=2, column=0, sticky="w")

# Adding Dropdown and Buttons
choices = ['1', '2', '3', '42', '100', '121002']
dropdown = tk.StringVar(root)
dropdown.set(choices[0])  # default value
popupMenu = tk.OptionMenu(root, dropdown, *choices)
popupMenu.grid(row=1, column=1, sticky="ew")

button = tk.Button(root, text="Click Me!")
button.grid(row=1, column=2, sticky="ew")

root.mainloop()