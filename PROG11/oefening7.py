from tkinter import *

def onclick1():
    getal1 = int(entry1.get())
    getal2 = int(entry2.get())
    plus = getal1 + getal2
    outcome = f"{getal1} + {getal2} = {plus}"
    label["text"] = outcome

def onclick2():
    getal1 = int(entry1.get())
    getal2 = int(entry2.get())
    keer = getal1 * getal2
    outcome = f"{getal1} * {getal2} = {keer}"
    label["text"] = outcome

root = Tk()

label = Label(master=root, text='Hello World', height=2)
label.pack()

button1 = Button(master=root, text='plus', command=onclick1)
button1.pack(pady=10)

button2 = Button(master=root, text='keer', command=onclick2)
button2.pack(pady=10)

entry1 = Entry(master=root)
entry1.pack(padx=10, pady=10)

entry2 = Entry(master=root)
entry2.pack(padx=10, pady=10)

root.mainloop()
