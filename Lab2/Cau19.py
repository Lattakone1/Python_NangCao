import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Python GUI")

# Define the exit function
def on_exit():
    root.quit()

# Define the about function
def show_about():
    messagebox.showinfo("About", "This is a Python GUI example.")

# Create the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=on_exit)

# Create Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Create the Tab Control
tabControl = ttk.Notebook(root)

# Create Tab1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

# Widgets for Tab1
label_frame = ttk.LabelFrame(tab1, text="Mighty Python")
label_frame.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(label_frame, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entry = ttk.Entry(label_frame, width=12, textvariable=name)
name_entry.grid(column=0, row=1, sticky='W')

ttk.Label(label_frame, text="Choose a number:").grid(column=1, row=0, sticky='W')
number = tk.StringVar()
number_chosen = ttk.Combobox(label_frame, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100, 300)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

action_button = ttk.Button(label_frame, text="Click Me!")
action_button.grid(column=2, row=1)

# Add a text box at the bottom of Tab1
text_box = tk.Text(tab1, height=5, width=40)
text_box.grid(column=0, row=2, padx=8, pady=8)

# Create Tab2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

# Widgets for Tab2
frame_check = ttk.LabelFrame(tab2, text="The Snake")
frame_check.grid(column=0, row=0, padx=8, pady=4)

# Checkbutton states
ch_var_dis = tk.IntVar()
check1 = tk.Checkbutton(frame_check, text="Disabled", variable=ch_var_dis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)

ch_var_un = tk.IntVar()
check2 = tk.Checkbutton(frame_check, text="Unchecked", variable=ch_var_un)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W)

ch_var_en = tk.IntVar()
check3 = tk.Checkbutton(frame_check, text="Enabled", variable=ch_var_en)
check3.select()
check3.grid(column=2, row=0, sticky=tk.W)

# Add Radio Buttons to change background color (moved above Labels in a Frame)
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        root.configure(background="blue")
    elif radSel == 1:
        root.configure(background="gold")
    elif radSel == 2:
        root.configure(background="red")

radVar = tk.IntVar()
radVar.set(99)  # Default value not selected

colors = ["Blue", "Gold", "Red"]
for col in range(3):
    curRad = tk.Radiobutton(tab2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=1, sticky=tk.W)

# Labels in a Frame (below Radio Buttons)
labels_frame = ttk.LabelFrame(tab2, text="Labels in a Frame")
labels_frame.grid(column=0, row=2, pady=8)

for i in range(3):
    ttk.Label(labels_frame, text=f"Label{i+1}").grid(column=i, row=0)

# Pack the tab control in the main window
tabControl.pack(expand=1, fill="both")

# Run the application
root.mainloop()
