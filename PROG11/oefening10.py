from tkinter import *

def maak_rood():
    root["background"] = "red"

def maak_groen():
    root["background"] = "green"

def maak_blauw():
    root["background"] = "blue"

root = Tk()

label = Label(root, text="Kies een kleur", height=2)
label.pack(pady=10)

button_rood = Button(root, text="Rood", command=maak_rood)
button_rood.pack(pady=5)

button_groen = Button(root, text="Groen", command=maak_groen)
button_groen.pack(pady=5)

button_blauw = Button(root, text="Blauw", command=maak_blauw)
button_blauw.pack(pady=5)

root.mainloop()