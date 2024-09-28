import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Longer Label Example")

# Tạo LabelFrame với padding
lf = ttk.LabelFrame(root, text="Labels in a Frame", padding=(10, 10, 10, 10))
lf.grid(column=0, row=0, padx=10, pady=10)

# Thêm các label, trong đó Label1 có nội dung dài hơn
ttk.Label(lf, text="Label1 -- sooooo much loooonger...").grid(column=0, row=0)
ttk.Label(lf, text="Label2").grid(column=0, row=1)
ttk.Label(lf, text="Label3").grid(column=0, row=2)

root.mainloop()