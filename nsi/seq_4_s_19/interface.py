from tkinter import *


def moov():
    global i
    drawing_space.delete("first")
    drawing_space.create_rectangle(100 + i, 100, 200 + i, 200, tags="first")
    i += 1
    ihm.after(50, moov)


i = 0

ihm = Tk()

drawing_space = Canvas(ihm, height=500, width=500)

drawing_space.pack()

moov()

ihm.mainloop()
