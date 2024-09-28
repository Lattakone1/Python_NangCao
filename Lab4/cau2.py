import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Tạo Spinbox với một tập hợp số
values = [1, 2, 3, 5, 7, 11]  # Các số cụ thể
spin = tk.Spinbox(root, values=values)  # Sử dụng 'values' thay vì 'values='
spin.pack()

# Callback của Spinbox
def _spin():
    value = spin.get()  # Lấy giá trị từ Spinbox
    print(value)        # In giá trị ra console
    return value

# Nút để lấy giá trị của Spinbox
button = tk.Button(root, text="Get Value", command=_spin)
button.pack()

# Hiển thị GUI
root.mainloop()
