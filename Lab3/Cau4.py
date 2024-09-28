import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Tạo cửa sổ chính
root = tk.Tk()

# Thiết lập tiêu đề của cửa sổ
root.title("Python GUI")

# Thay đổi biểu tượng của cửa sổ
root.iconbitmap('D:/Lập trình Python nâng cao/Lab3/my_icon.ico')  # Đảm bảo rằng đường dẫn đúng

# Tạo hàm xử lý khi bấm vào "Exit"
def on_exit():
    root.quit()

# Tạo hàm xử lý khi bấm vào "About"
def show_about():
    messagebox.showinfo("About", "This is a Python GUI example.\nCreated using Tkinter.")

# Tạo Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Tạo menu "File" với "New" và "Exit"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")  # Menu New
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)  # Menu Exit
menu_bar.add_cascade(label="File", menu=file_menu)

# Tạo menu "Help" với "About"
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)  # Menu About
menu_bar.add_cascade(label="Help", menu=help_menu)

# Tạo Tab Control
tab_control = ttk.Notebook(root)

# Tạo Tab 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')

# Tạo LabelFrame trong Tab 1
label_frame = ttk.LabelFrame(tab1, text="Mighty Python")
label_frame.grid(column=0, row=0, padx=8, pady=4)

# Tạo các widget trong LabelFrame
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

# Thêm một Text box ở dưới Tab 1
text_box = tk.Text(tab1, height=5, width=40)
text_box.grid(column=0, row=2, padx=8, pady=8)

# Tạo Tab 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')

# Hiển thị Tab Control
tab_control.pack(expand=1, fill="both")

# Chạy chương trình
root.mainloop()
