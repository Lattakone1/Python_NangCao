import tkinter as tk

# Function to handle button click event
def on_click():
    print("Button clicked!")
    print(f"Name entered: {entry.get()}")
    print(f"Number chosen: {combo.get()}")
    print(f"Disabled: {disabled.get()}")
    print(f"Unchecked: {unchecked.get()}")
    print(f"Enabled: {enabled.get()}")

# Create the main window
window = tk.Tk()
window.title("Python GUI")

# Create a label
label = tk.Label(window, text="Enter a name:")
label.grid(column=0, row=0)

# Create an entry widget
entry = tk.Entry(window, width=20)
entry.grid(column=1, row=0)

# Create a ComboBox (drop-down menu)
combo = tk.StringVar(value="Choose a number:")
combo_box = tk.OptionMenu(window, combo, "42", "1", "2", "3", "4", "5")
combo_box.grid(column=2, row=0)

# Create CheckButtons (Checkboxes)
disabled = tk.BooleanVar()
disabled.set(False)
chk_disabled = tk.Checkbutton(window, text='Disabled', var=disabled)
chk_disabled.grid(column=0, row=1)

unchecked = tk.BooleanVar()
unchecked.set(False)
chk_unchecked = tk.Checkbutton(window, text='UnChecked', var=unchecked)
chk_unchecked.grid(column=1, row=1)

enabled = tk.BooleanVar()
enabled.set(True)
chk_enabled = tk.Checkbutton(window, text='Enabled', var=enabled)
chk_enabled.grid(column=2, row=1)

# Create a Button
button = tk.Button(window, text="Click Me!", command=on_click)
button.grid(column=2, row=2)
# Run the application
window.mainloop()
