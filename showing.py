# -*- coding: utf-8 -*-
from config import *
from tkinter import *






class Showing:

    """ по сути это поле, это - канвас """

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')





canvas = Showing()


class Entity:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect_id = canvas.canvas.create_rectangle(self.x, self.y, self.x + step, self.y + step, fill=self.color)


    def coords(self):
        return canvas.canvas.coords(self.rect_id)


    def move(self, x, y):

        canvas.canvas.move(self.rect_id, x, y)
