#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, BOTH, Canvas

class Example():
    def __init__(self, parent):
        #Canvas.__init__(self, parent, width = 500, height = 500, background="black")
        self.parent = parent


    def create(self,x,y, color):
        self.rect = self.parent.create_rectangle(x,y,x+10,y+10,fill = color)


    def move_hero(self):  # движение
        self.parent.bind('<w>', lambda event: self.parent.move(self.rect, 0, -10))
        self.parent.bind('<s>', lambda event: self.parent.move(self.rect, 0, 10))
        self.parent.bind('<a>', lambda event: self.parent.move(self.rect, -10, 0))
        self.parent.bind('<d>', lambda event: self.parent.move(self.rect, 10, 0))
        self.parent.after(30, move_hero)


def main():
    root = Tk()
    c = Canvas(root, width = 500, height = 500, background="black")
    c.pack()
    root.bind('<w>', lambda event: self.parent.move(self.rect, 0, -10))
    root.bind('<s>', lambda event: self.parent.move(self.rect, 0, 10))
    root.bind('<a>', lambda event: self.parent.move(self.rect, -10, 0))
    root.bind('<d>', lambda event: self.parent.move(self.rect, 10, 0))
    app = Example(c)
    app.create(10,10,"white")
    app.move_hero()
    a = Example(c)
    a.create(40,40,"green")


    root.mainloop()

if __name__ == '__main__':
    main()


#root = Tk()
#c = Canvas(self.root, width=300, height=300, bg='white')
#c.pack()



#root.mainloop()
