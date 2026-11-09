from tkinter import *

root = Tk()

label = Label(root, text="Kies een getal")
label.grid(row=0, column=0, columnspan=4)

for row in range(1,4):
    for col in range(4):
        number = (col+1)+(row*4)
        button = Button(master=root, text=f'{number}')
        button.grid(row=row, column=col, pady=4)
root.mainloop()

