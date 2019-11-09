from tkinter import *


class MainInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title()
        self.root.geometry("500x500")
        self.canvas = Canvas(self.root, width = 500, height = 500, bg = 'black')
        self.canvas.pack()
        self.x = 100
        self.y = 100
        self.create()
        self.show()





    def create(self):
        self.object =  self.canvas.create_rectangle(self.x, self.y, self.x + 10,self.y + 10, fill = "green")


    def show(self):
        self.x += 10
        self.y -= 10
        print(self.x, self.y)
        self.canvas.move(self.object, self.x, self.y)
        self.canvas.after(1000, self.show)


program = MainInterface()
program.root.mainloop()
