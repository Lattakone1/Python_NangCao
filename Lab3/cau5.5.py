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

# Tạo hàm để cập nhật Text box với giá trị Spinbox
def update_textbox(*args):
    current_value = spin_value.get()
    # Kiểm tra xem giá trị có nằm trong danh sách (1, 2, 4, 42, 100) không
    if current_value in values:
        # Thêm dòng mới vào Text box mà không xóa nội dung cũ
        text_box.insert(tk.END, f"{current_value}\n")
        text_box.insert(tk.END, "1\n")
        text_box.insert(tk.END, "2\n")
        text_box.insert(tk.END, "3\n")

# Tạo danh sách giá trị cho Spinbox
values = [1, 2, 4, 42, 100]

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

# Thêm Spinbox với viền 3D
ttk.Label(label_frame, text="Select a value (1, 2, 4, 42, 100):").grid(column=0, row=2, sticky='W')
spin_value = tk.IntVar()  # Biến lưu giá trị Spinbox
spin_value.trace_add("write", update_textbox)  # Thêm callback

spinbox_frame = ttk.Frame(label_frame, borderwidth=6, relief='raised')  # Tạo frame với viền
spinbox_frame.grid(column=0, row=3, sticky='W')

# Đặt Spinbox vào frame
spinbox = ttk.Spinbox(spinbox_frame, from_=1, to=100, textvariable=spin_value, width=5)
spinbox.pack()

# Thêm nút "Click Me!"
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
