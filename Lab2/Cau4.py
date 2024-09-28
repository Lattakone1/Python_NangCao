import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("More Padding Example")

# Tạo LabelFrame với padding lớn hơn
lf = ttk.LabelFrame(root, text="Labels in a Frame", padding=(20, 20, 20, 20))
lf.grid(column=0, row=0, padx=20, pady=20)

# Thêm các label
ttk.Label(lf, text="Label1").grid(column=0, row=0)
ttk.Label(lf, text="Label2").grid(column=0, row=1)
ttk.Label(lf, text="Label3").grid(column=0, row=2)

root.mainloop()