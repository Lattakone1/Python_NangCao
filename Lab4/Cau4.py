import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ToolTip:
    """Class to create a tooltip for any widget."""

    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Remove window decorations
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(tw, text=self.text, justify='left',
                         background="lightyellow", relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class App:
    """Main application class."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI")
        self.root.iconbitmap('D:/Lập trình Python nâng cao/Lab3/my_icon.ico')  # Replace with a valid icon path

        self.create_menu()
        self.create_tabs()

    def create_menu(self):
        """Create the menu bar with File and Help options."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_exit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def create_tabs(self):
        """Create tab control with two tabs."""
        tab_control = ttk.Notebook(self.root)

        # Tab 1
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Tab 1')

        self.create_tab1_widgets(tab1)

        # Tab 2
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Tab 2')

        tab_control.pack(expand=1, fill="both")

    def create_tab1_widgets(self, parent):
        """Create widgets for Tab 1."""
        label_frame = ttk.LabelFrame(parent, text="Hello GUI")
        label_frame.grid(column=0, row=0, padx=8, pady=4)

        # Label and Entry for name
        ttk.Label(label_frame, text="Enter a name:").grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        self.name_entry = ttk.Entry(label_frame, width=12, textvariable=self.name)
        self.name_entry.grid(column=0, row=1, sticky='W')
        ToolTip(self.name_entry, "Enter your name here")

        # Combobox for number selection
        ttk.Label(label_frame, text="Choose a number:").grid(column=1, row=0, sticky='W')
        self.number = tk.StringVar()
        self.number_chosen = ttk.Combobox(label_frame, width=12, textvariable=self.number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100, 300)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)
        ToolTip(self.number_chosen, "Choose a number from the dropdown")

        # Spinbox for value selection
        ttk.Label(label_frame).grid(column=0, row=2, sticky='W')
        self.spin_value = tk.IntVar()
        self.spinbox = ttk.Spinbox(label_frame, from_=-1000, to=1000, textvariable=self.spin_value, width=5)
        self.spinbox.grid(column=0, row=3, sticky='W')
        ToolTip(self.spinbox, "Spin to select a value")

        # Button with click action
        self.action_button = ttk.Button(label_frame, text="Click Me!", command=self.on_button_click)
        self.action_button.grid(column=2, row=1)
        ToolTip(self.action_button, "Click to execute action")

        # Text box for displaying information
        self.text_box = tk.Text(parent, height=5, width=40)
        self.text_box.grid(column=0, row=2, padx=8, pady=8)

    def on_button_click(self):
        """Handle the button click event."""
        spin_value = self.spin_value.get()
        output = f"GUI_OOP_2_classes.py\nSpinbox value: {spin_value}\n"
        self.text_box.insert(tk.INSERT, output)

    def on_exit(self):
        """Handle the exit event."""
        self.root.quit()

    def show_about(self):
        """Show the 'About' message box."""
        messagebox.showinfo("About", "This is a Python GUI example.\nCreated using Tkinter.")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
