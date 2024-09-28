import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Python GUI")

# Define the exit function
def on_exit():
    root.quit()  # Quits the application

# Define the about function with Yes/No/Cancel dialog
def show_about():
    result = messagebox.askyesnocancel("Python Message Box", "Do you want to continue?")
    if result is True:
        messagebox.showinfo("Result", "You chose YES.")
    elif result is False:
        messagebox.showinfo("Result", "You chose NO.")
    else:
        messagebox.showinfo("Result", "You chose CANCEL.")

# Define the warning function
def show_warning():
    messagebox.showwarning("Python Message Warning Box", "Warning: There might be a bug in this code.")

# Define the error function
def show_error():
    messagebox.showerror("Python Message Error Box", "Error: Houston ~ we do have a serious PROBLEM!")

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
help_menu.add_command(label="About", command=show_about)  # Updated About command
help_menu.add_command(label="Warning", command=show_warning)
help_menu.add_command(label="Error", command=show_error)

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

# Define the function to change LabelFrame color based on Radio Button selection
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        labels_frame.configure(style="Blue.TLabelframe")  # Change LabelFrame to blue
    elif radSel == 1:
        labels_frame.configure(style="Gold.TLabelframe")  # Change LabelFrame to gold
    elif radSel == 2:
        labels_frame.configure(style="Red.TLabelframe")   # Change LabelFrame to red

# Initialize radio button variable
radVar = tk.IntVar()
radVar.set(99)  # Default value (none selected)

# Create Radio Buttons for color selection
colors = ["Blue", "Gold", "Red"]
for col in range(3):
    curRad = tk.Radiobutton(tab2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=1, sticky=tk.W)

# Labels in a Frame (LabelFrame that will change color based on Radio Button selection)
labels_frame = ttk.LabelFrame(tab2, text="Labels in a Frame")
labels_frame.grid(column=0, row=2, pady=8)

# Configure styles for LabelFrame colors
style = ttk.Style()
style.configure("Blue.TLabelframe", background="blue")
style.configure("Gold.TLabelframe", background="gold")
style.configure("Red.TLabelframe", background="red")

for i in range(3):
    ttk.Label(labels_frame, text=f"Label{i+1}").grid(column=i, row=0)

# Pack the tab control in the main window
tabControl.pack(expand=1, fill="both")

# Run the application
root.mainloop()
