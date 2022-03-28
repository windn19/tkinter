from tkinter import Tk, Entry, Button, Label, LEFT, Frame, END, StringVar
from tkinter.messagebox import showinfo
from math import ceil, sqrt


def add_val(arg=None):
    print(arg)
    val = entry.get().strip()
    if not (val.isdigit() or (val[1:].isdigit() and val[0] == '-')):
        entry.delete(0, END)
        return showinfo('Stop', "Ожидается ввод только цифр")
    else:
        val = int(val)
    # if not val % 2:
    #     showinfo('Stop', 'Получен четный элемент')
    #     return window.destroy()
    lbl['text'] = '\n'.join([f'{x:^5} - {x ** 2:^5}' for x in range(2, ceil(sqrt(val))+1)])
    entry.delete(0, END)


def modify(*args):
    t = text.get()
    if t and t[-1] not in {*list(map(str, range(10))), '-'}:
        print('yes')
        text.set(t[:-1])


window = Tk()
window.title('Сумма')
# ws = window.winfo_screenwidth()
# hs = window.winfo_screenheight()
# w = 300
# h = 80
# x = (ws // 2) - (w // 2)
# y = (hs // 2) - (h // 2)
# print(ws, hs)
# print(x, y)
window.geometry('+700+350')
window.columnconfigure(0, minsize=1000)
window.rowconfigure(0, minsize=1000)
# print(window.winfo_screenwidth(), window.winfo_screenheight())

text = StringVar()

bt_frame = Frame(master=window, padx=5, pady=5)
but = Button(master=bt_frame, text='Close', command=window.destroy)
but_work = Button(master=bt_frame, text='Add', command=add_val)
but.grid(column=0, row=1, sticky='NSEW')
but_work.grid(column=0, row=0, sticky='NSEW')
entry = Entry(master=window, textvariable=text)
lbl = Label(master=window)

entry.pack(side=LEFT, padx=5, pady=5)
bt_frame.pack(side=LEFT, padx=5, pady=5)
lbl.pack(side=LEFT, padx=5, pady=5)

entry.focus_set()
entry.bind('<Key-Return>', add_val)
entry.bind('<Key-Escape>', lambda x: window.destroy())
text.trace('w', modify)

window.mainloop()
