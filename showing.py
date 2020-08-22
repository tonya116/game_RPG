# -*- coding: utf-8 -*-
from tkinter import *


WIDTH = 640
HEIGHT = 480


class Showing:

    """ по сути это поле, это - канвас """

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.grid()


canvas = Showing()

class Entity:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect_id = canvas.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)


    def coords(self):
        return canvas.canvas.coords(self.rect_id)
