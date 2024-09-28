import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Remove Title Example")

# Tạo LabelFrame nhưng không có tiêu đề
lf = ttk.LabelFrame(root, padding=(10, 10, 10, 10))
lf.grid(column=0, row=0, padx=10, pady=10)

# Thêm các label
ttk.Label(lf, text="Label1").grid(column=0, row=0)
ttk.Label(lf, text="Label2").grid(column=0, row=1)
ttk.Label(lf, text="Label3").grid(column=0, row=2)

root.mainloop()