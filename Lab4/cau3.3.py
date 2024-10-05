import tkinter as tk
from tkinter import ttk

# Biến toàn cục
GLOBAL_CONST = 42
print("GLOBAL_CONST:", GLOBAL_CONST)  # In ra giá trị của biến toàn cục

# Tạo ứng dụng GUI
root = tk.Tk()  # Tạo cửa sổ chính
root.title("Simple GUI")  # Đặt tiêu đề cho cửa sổ

# Tạo Entry widget để nhập tên
name_label = ttk.Label(root, text="Enter your name:")
name_label.grid(column=0, row=0)

name_entered = ttk.Entry(root, width=12)  # Ô nhập liệu cho tên
name_entered.grid(column=1, row=0)
name_entered.focus()  # Focus vào ô nhập liệu

# Hàm sử dụng biến toàn cục nhưng không thay đổi giá trị của nó
def usingGlobal():
    print("GLOBAL_CONST in function:", GLOBAL_CONST)

# Gọi hàm để in giá trị của biến toàn cục
usingGlobal()

# Ghi đè giá trị biến toàn cục bằng biến cục bộ
def modifyGlobal():
    global GLOBAL_CONST  # Sử dụng từ khóa global để thay đổi giá trị biến toàn cục
    GLOBAL_CONST = 777   # Thay đổi giá trị biến toàn cục

# Gọi hàm để sửa đổi giá trị
modifyGlobal()

# In giá trị của biến toàn cục sau khi thay đổi
print("GLOBAL_CONST after modification:", GLOBAL_CONST)

# Khởi chạy GUI
root.mainloop()
