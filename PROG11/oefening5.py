from tkinter import *

def onclick():
    label["text"] = entry.get()

root = Tk()

label = Label(master=root, text='Hello World', height=2)
label.pack()

button = Button(master=root, text='Press', command=onclick)
button.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()
