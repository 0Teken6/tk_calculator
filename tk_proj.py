import tkinter as tk


sign = False
total = 0


def clear():
    global total
    total = 0
    main_lbl['text'] = str(total)

def default(num):
    global total, sign, main_lbl
    if sign:
        if sign == '/' and num == 0:
            main_lbl['text'] = 'На 0 делить нельзя'
            total = 0
            sign = False
            return
        total = eval(f'{total}{sign}{num}')
        main_lbl['text'] = str(total)
        sign = False
    else:
        total = num
        main_lbl['text'] = str(total)

    print(num)


def add():
    global sign
    sign = '+'
    print(sign)

def minus():
    global sign
    sign = '-'
    print(sign)

def mult():
    global sign
    sign = '*'
    print(sign)

def devide():
    global sign
    sign = '/'
    print(sign)


win = tk.Tk()

win.rowconfigure([0, 1], minsize=25)
win.columnconfigure([0, 1], minsize=25)
win.resizable(width=False, height=False)

main_lbl = tk.Label(text=f'{total}', bg='grey', fg='white')
main_lbl.grid(column=0, row=0, sticky='e')

sign_frm = tk.Frame(master=win)
sign_frm.grid(row=1, column=1, sticky='nsew')
sign_frm.rowconfigure([0, 1, 2, 3], minsize=50)
sign_frm.columnconfigure(0, minsize=50)
but_add = tk.Button(command=add, text="+", master=sign_frm)
but_add.grid(column=0, row=0, sticky='nsew')
but_add = tk.Button(command=minus, text="-", master=sign_frm)
but_add.grid(column=0, row=1, sticky='nsew')
but_add = tk.Button(command=mult, text="*", master=sign_frm)
but_add.grid(column=0, row=2, sticky='nsew')
but_add = tk.Button(command=devide, text="/", master=sign_frm)
but_add.grid(column=0, row=3, sticky='nsew')

digits_frm = tk.Frame()
digits_frm.rowconfigure([0, 1, 2, 3], minsize=50)
digits_frm.columnconfigure([0, 1, 2], minsize=50)
digits_frm.grid(column=0, row=1, sticky='nsew')


but = tk.Button(text="1", master=digits_frm, command=lambda: default(1))
but.grid(column=0, row=0, sticky='nsew')
but = tk.Button(text=f"2", master=digits_frm, command=lambda: default(2))
but.grid(column=1, row=0, sticky='nsew')
but = tk.Button(text=f"3", master=digits_frm, command=lambda: default(3))
but.grid(column=2, row=0, sticky='nsew')
but = tk.Button(text=f"4", master=digits_frm, command=lambda: default(4))
but.grid(column=0, row=1, sticky='nsew')
but = tk.Button(text=f"5", master=digits_frm, command=lambda: default(5))
but.grid(column=1, row=1, sticky='nsew')
but = tk.Button(text=f"6", master=digits_frm, command=lambda: default(6))
but.grid(column=2, row=1, sticky='nsew')
but = tk.Button(text=f"7", master=digits_frm, command=lambda: default(7))
but.grid(column=0, row=2, sticky='nsew')
but = tk.Button(text=f"8", master=digits_frm, command=lambda: default(8))
but.grid(column=1, row=2, sticky='nsew')
but = tk.Button(text=f"9", master=digits_frm, command=lambda: default(9))
but.grid(column=2, row=2, sticky='nsew')
but = tk.Button(text=f"C", master=digits_frm, command=clear)
but.grid(column=0, row=3, sticky='nsew')
but = tk.Button(text=f"0", master=digits_frm, command=lambda: default(0))
but.grid(column=1, row=3, sticky='nsew')

win.mainloop()
