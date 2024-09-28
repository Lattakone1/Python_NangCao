import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Modified Button Click Function
def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())

# GUI Callback function
def checkCallback(*ignoredArgs):
    if chVarUn.get():
        check3.configure(state='disabled')
        check1.config(state='normal')
    else:
        check3.configure(state='normal')
    if chVarEn.get():
        check1.configure(state='disabled')
        check2.configure(state='disabled')
    else:
        check1.configure(state='normal')
        check2.configure(state='normal')

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])

if __name__ == '__main__':

    win = tk.Tk()
    win.title("Python GUI")

    # Adding labels and widgets
    ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

    # Adding a Textbox Entry widget
    name = tk.StringVar()
    name_entered = ttk.Entry(win, width=12, textvariable=name)
    name_entered.grid(column=0, row=1)
    name_entered.focus()

    # Adding a Button
    action = ttk.Button(win, text="Click Me!", command=click_me)
    action.grid(column=2, row=1)

    ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
    number = tk.StringVar()
    number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
    number_chosen['values'] = (1, 2, 4, 42, 100)
    number_chosen.grid(column=1, row=1)
    number_chosen.current(0)

    # Creating three checkbuttons
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
    check3.deselect()
    check3.grid(column=2, row=4, sticky=tk.W)

    # Trace the state of the two checkbuttons
    chVarUn.trace_add('write', lambda *args: checkCallback())
    chVarEn.trace_add('write', lambda *args: checkCallback())

    # Using a scrolled Text control (without columnspan)
    scrol_w = 30
    scrol_h = 3
    scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
    scr.grid(column=0, row=5)

    # Radiobuttons with background color change
    colors = ["Blue", "Gold", "Light Gray"]

    radVar = tk.IntVar()
    radVar.set(2)
    radCall()

    for col in range(3):
        curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
                                value=col, command=radCall)
        curRad.grid(column=col, row=6, sticky=tk.W)

    # Creating a container for labels
    buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
    buttons_frame.grid(column=0, row=7, columnspan=3, pady=10)

    # Placing labels into the container
    ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
    ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
    ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

    name_entered.focus()  # Focus cursor in name entry box
    win.mainloop()
