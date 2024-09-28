import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background="blue")
    elif radSel == 1:
        win.configure(background="gold")
    elif radSel == 2:
        win.configure(background="red")

# Click event handler
def click_me():
    action.configure(text="Hello " + name.get())

if __name__ == '__main__':
    win = tk.Tk()
    win.title("Python GUI")

    # Adding labels and widgets
    ttk.Label(win, text="Enter a name:").grid(column=0, row=0, sticky=tk.W)

    # Adding a Textbox Entry widget
    name = tk.StringVar()
    name_entered = ttk.Entry(win, width=12, textvariable=name)
    name_entered.grid(column=0, row=1)
    name_entered.focus()

    # Adding a Button
    action = ttk.Button(win, text="Click Me!", command=click_me)
    action.grid(column=2, row=1)

    # Combobox for number selection
    ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
    number = tk.StringVar()
    number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
    number_chosen['values'] = (1, 2, 4, 42, 100)
    number_chosen.grid(column=1, row=1)
    number_chosen.current(0)

    # Creating checkbuttons
    chVarDis = tk.IntVar()
    check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
    check1.select()
    check1.grid(column=0, row=4, sticky=tk.W)

    chVarUn = tk.IntVar()
    check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
    check2.deselect()
    check2.grid(column=1, row=4, sticky=tk.W)

    chVarEn = tk.IntVar()
    check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
    check3.select()
    check3.grid(column=2, row=4, sticky=tk.W)

    # Scroll Text box
    scrol_w = 30
    scrol_h = 3
    scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
    scr.grid(column=0, row=5, columnspan=3)

    # Radiobuttons for changing the background color
    radVar = tk.IntVar()
    radVar.set(99)

    colors = ["Blue", "Gold", "Red"]
    for col in range(3):
        curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
                                value=col, command=radCall)
        curRad.grid(column=col, row=6, sticky=tk.W)

    # LabelFrame for containing labels (Moved below the Radiobuttons)
    buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
    buttons_frame.grid(column=0, row=7)

    ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
    ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
    ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

    # Start GUI
    win.mainloop()
