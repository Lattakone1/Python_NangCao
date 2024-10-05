import tkinter as tk
from tkinter import ttk

# Biến toàn cục
GLOBAL_CONST = 42
print(GLOBAL_CONST)  # In ra giá trị của biến toàn cục

# Tạo ứng dụng GUI
root = tk.Tk()  # Tạo cửa sổ chính
root.title("Simple GUI")  # Đặt tiêu đề cho cửa sổ

# Tạo Entry widget để nhập tên
name_label = ttk.Label(root, text="Enter your name:")
name_label.grid(column=0, row=0)

name_entered = ttk.Entry(root, width=12)  # Ô nhập liệu cho tên
name_entered.grid(column=1, row=0)
name_entered.focus()  # Focus vào ô nhập liệu

# Khởi chạy GUI
win = root
win.mainloop()
