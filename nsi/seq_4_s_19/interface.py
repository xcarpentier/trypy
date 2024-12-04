from tkinter import Tk, Canvas


def moving_rectangle():
    global i
    drawing_space.delete("jauge")
    color = (
        "green"
        if i <= 100
        else "yellow" if i <= 150 else "orange" if i <= 175 else "red"
    )
    if i <= 200:
        drawing_space.delete("second")
        drawing_space.create_rectangle(
            300,
            300,
            400,
            300 - i,
            tags="second",
            fill=color,
        )
        i += 1
    if 175 <= i <= 200:
        drawing_space.create_text(
            150,
            200,
            text="La jauge est presque pleine !",
            font=("Arial", 15),
            tags="jauge",
        )
    elif i > 200:
        drawing_space.create_text(
            150, 200, text="La jauge est pleine !", font=("Arial", 15), tags="jauge"
        )
    drawing_space.create_text(
        150,
        175,
        text=f"{round(i*100/200)} %",
        font=("Arial", 15),
        fill=color,
        tags="jauge",
    )
    drawing_space.after(50, moving_rectangle)


def decrease():
    global i
    i = 1


i = 0

ihm = Tk()
drawing_space = Canvas(ihm, height=500, width=500)
drawing_space.pack()
drawing_space.create_rectangle(300, 300, 400, 100, tags="first")

moving_rectangle()
ihm.bind("v", lambda _: decrease())

ihm.mainloop()
