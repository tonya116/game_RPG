import humans
import tkinter as tk
from random import randint

WIDTH = 500
HEIGHT = 500


class Showing:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.rect_id = canvas.create_rectangle(
                                    self.x,
                                    self.y,
                                    self.x + 10,
                                    self.y + 10,
                                    fill="green")




    def show(self):
        
        canvas.coords(self.rect_id, self.x, self.y, self.x + 10, self.y + 10)

    def move(self, event):

        if event.char == "w":
            self.y -= 10
        if event.char == "s":
            self.y += 10
        if event.char == "a":
            self.x -= 10
        if event.char == "d":
            self.x += 10

    def get_button(self):
        canvas.bind('<Key>', self.move)


hero = humans.Humans(20, "Den", "Human", 100, 1, 1, 1, 1, 100)


def tick():

        obj.show()
        obj.get_button()
        root.after(10, tick)


def main():
    global root, canvas, obj

    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root, width=500, height=500, bg = "black")

    canvas.pack()

    obj = Showing()

    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
