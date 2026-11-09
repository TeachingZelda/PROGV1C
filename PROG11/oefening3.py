

from tkinter import *







root = Tk()

label = Label(master=root,
              text='Hello World',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'),
              width=15,
              height=8)
label.pack()

root.mainloop()