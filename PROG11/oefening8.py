from tkinter import *
from functools import partial

def onclick(message):
    label["text"] = message

root = Tk()

label = Label(master=root, text='Hello World', height=2)
label.pack()

buttonA = Button(master=root, text='A', command=partial(onclick, "Message from A"))
buttonA.pack()

buttonB = Button(master=root, text='B', command=partial(onclick, "Message from B"))
buttonB.pack(pady=10)

root.mainloop()

