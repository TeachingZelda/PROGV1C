from tkinter import *

root = Tk()

img = PhotoImage(file='beach.png')
label = Label(master=root, image=img)
label.pack()

root.mainloop()

