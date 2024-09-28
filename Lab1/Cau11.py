import tkinter as tk
from tkinter import scrolledtext

def on_click():
    # This function will append text to the ScrolledText widget
    text_widget.insert(tk.END, "\nsuccessfully in millions of real-world business solutions all over this globe..")

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
combo_box = tk.OptionMenu(window, combo, "1", "2", "3", "4", "5")
combo_box.grid(column=2, row=0)

# Create CheckButtons
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

# Create radio buttons
colors = ["Blue", "Gold", "Red"]
color_var = tk.StringVar()
color_var.set(colors[0])  # Default value

for idx, color in enumerate(colors):
    radio_btn = tk.Radiobutton(window, text=color, value=color, variable=color_var)
    radio_btn.grid(column=idx, row=2)

# Create a ScrolledText widget
text_widget = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
text_widget.grid(column=0, row=3, columnspan=3)
text_widget.insert(tk.END, "A multi-line ScrolledText widget written in Python...")

# Create a Button to append text
button = tk.Button(window, text="Click Me!", command=on_click)
button.grid(column=2, row=4)

# Run the application
window.mainloop()
