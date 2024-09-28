import tkinter as tk
from tkinter import ttk

# Hàm để thay đổi màu của LabelFrame
def change_color():
    selected_color = color_choice.get()
    if selected_color == 'Blue':
        lf.config(style="Blue.TLabelframe")
    elif selected_color == 'Gold':
        lf.config(style="Gold.TLabelframe")
    elif selected_color == 'Red':
        lf.config(style="Red.TLabelframe")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("LabelFrame Padding with Color Options")

# Thiết lập các kiểu màu cho LabelFrame
style = ttk.Style()
style.configure("Blue.TLabelframe", background="blue")
style.configure("Gold.TLabelframe", background="gold")
style.configure("Red.TLabelframe", background="red")

# Tạo LabelFrame với padding
lf = ttk.LabelFrame(root, text="Labels in a Frame", padding=(10, 10, 10, 10))
lf.grid(column=0, row=1, padx=10, pady=10)

# Thêm các label vào bên trong LabelFrame
ttk.Label(lf, text="Label1").grid(column=0, row=0)
ttk.Label(lf, text="Label2").grid(column=0, row=1)
ttk.Label(lf, text="Label3").grid(column=0, row=2)

# Biến lưu lựa chọn màu sắc
color_choice = tk.StringVar(value="Blue")

# Tạo các nút radio để chọn màu
blue_radio = ttk.Radiobutton(root, text="Blue", variable=color_choice, value="Blue", command=change_color)
blue_radio.grid(column=0, row=0, sticky=tk.W)

gold_radio = ttk.Radiobutton(root, text="Gold", variable=color_choice, value="Gold", command=change_color)
gold_radio.grid(column=1, row=0, sticky=tk.W)

red_radio = ttk.Radiobutton(root, text="Red", variable=color_choice, value="Red", command=change_color)
red_radio.grid(column=2, row=0, sticky=tk.W)

# Chạy vòng lặp chính của ứng dụng
root.mainloop()