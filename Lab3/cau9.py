import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Tooltip class
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind('<Enter>', self.show_tooltip)
        self.widget.bind('<Leave>', self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tooltip_window is not None:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, background='yellow', borderwidth=1, relief='solid')
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# Main window setup
root = tk.Tk()
root.title("Python GUI")
root.iconbitmap('D:/Lập trình Python nâng cao/Lab3/my_icon.ico')  # Ensure correct path

# Exit handling
def on_exit():
    root.quit()

# About dialog
def show_about():
    messagebox.showinfo("About", "This is a Python GUI example.\nCreated using Tkinter.")

# Button click event
def on_click():
    greeting = f"Hello {name.get()}"  # Fetch the name and prepare greeting
    action_button.config(text=greeting)  # Update button text with the greeting

def update_textbox(event):
    # Check if the chosen number is one of the specific valid numbers
    if number.get() in ['1', '2', '4','5','88','42', '100', '300']:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "This is a ScrolledText Widget")
    else:
        text_box.delete(1.0, tk.END)

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Tabs setup
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')

# LabelFrame in Tab 1
label_frame = ttk.LabelFrame(tab1, text="Mighty Python")
label_frame.grid(column=0, row=0, padx=8, pady=4)

# Widgets in LabelFrame
ttk.Label(label_frame, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entry = ttk.Entry(label_frame, width=12, textvariable=name)
name_entry.grid(column=0, row=1, sticky='W')
ToolTip(name_entry, "Enter your name here")

ttk.Label(label_frame, text="Choose a number:").grid(column=1, row=0, sticky='W')
number = tk.StringVar()
number_chosen = ttk.Combobox(label_frame, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 3, 4, 5, 9, 54, 98, 34, 543, 56, 67, 432, 34, 54, 43, 42, 100, 300)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)
number_chosen.bind('<<ComboboxSelected>>', update_textbox)
ToolTip(number_chosen, "Select a number from the list")

# Button with action
action_button = ttk.Button(label_frame, text="Click Me!", command=on_click)
action_button.grid(column=2, row=1)
ToolTip(action_button, "Click to display your greeting")

# Text box in Tab 1
text_box = tk.Text(tab1, height=5, width=40)
text_box.grid(column=0, row=2, padx=8, pady=8)

# Additional tab
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')

# Widgets in Tab 2
# Checkboxes
chk_state_enabled = tk.BooleanVar()
chk_enabled = ttk.Checkbutton(tab2, text='Disabled', var=chk_state_enabled, state='disabled')
chk_enabled.grid(column=0, row=0, padx=8, pady=4)



chk_state_unchecked = tk.BooleanVar()
chk_unchecked = ttk.Checkbutton(tab2, text='Unchecked', var=chk_state_unchecked)
chk_unchecked.grid(column=1, row=0, padx=8, pady=4)

chk_state_disabled = tk.BooleanVar()
chk_disabled = ttk.Checkbutton(tab2, text='Enabled', var=chk_state_disabled)
chk_disabled.grid(column=2, row=0, padx=8, pady=4)

# Radio buttons for color choice
color = tk.StringVar()
red_radio = ttk.Radiobutton(tab2, text='Red', value='Red', variable=color)
blue_radio = ttk.Radiobutton(tab2, text='Blue', value='Blue', variable=color)
gold_radio = ttk.Radiobutton(tab2, text='Gold', value='Gold', variable=color)
red_radio.grid(column=0, row=4, padx=8, pady=4)
blue_radio.grid(column=1, row=4, padx=8, pady=4)
gold_radio.grid(column=2, row=4, padx=8, pady=4)

# Progress bar
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=200, mode='determinate')
progress_bar.grid(column=0, row=2, columnspan=3, padx=8, pady=4)

def stop_progressbar_after_second():
    root.after(1000, progress_bar.stop)

# Control buttons
run_button = ttk.Button(tab2, text="Run Progressbar", command=lambda: progress_bar.start(10))
start_button = ttk.Button(tab2, text="Start Progressbar", command=lambda: progress_bar.step(25))
stop_button = ttk.Button(tab2, text="Stop immediately", command=progress_bar.stop)
stop_after_sec_button = ttk.Button(tab2, text="Stop after second", command=stop_progressbar_after_second)

run_button.grid(column=0, row=3, padx=8, pady=4)
start_button.grid(column=1, row=3, padx=8, pady=4)
stop_button.grid(column=2, row=3, padx=8, pady=4)
stop_after_sec_button.grid(column=1, row=5, padx=8, pady=4)

# Additional tab for striped sections (Tab 3)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Tab 3')

# Create four equal frames in Tab 3
frame1 = tk.Frame(tab3, background='#FFD700', width=200, height=100)
frame2 = tk.Frame(tab3, background='#00008B', width=200, height=100)
frame3 = tk.Frame(tab3, background='#00008B', width=200, height=100)
frame4 = tk.Frame(tab3, background='#FFD700', width=200, height=100)

# Use grid to divide Tab 3 into four equal sections
frame1.grid(row=0, column=0, sticky='nsew')
frame2.grid(row=0, column=1, sticky='nsew')
frame3.grid(row=1, column=0, sticky='nsew')
frame4.grid(row=1, column=1, sticky='nsew')

# Configure rows and columns to stretch equally
tab3.grid_columnconfigure(0, weight=1)
tab3.grid_columnconfigure(1, weight=1)
tab3.grid_rowconfigure(0, weight=1)
tab3.grid_rowconfigure(1, weight=1)

# Display Tabs
tab_control.pack(expand=1, fill="both")


# Start the GUI
root.mainloop()
