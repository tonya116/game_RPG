# -*- coding: utf-8 -*-
from tkinter import *


WIDTH = 640
HEIGHT = 480


class Showing:

    """ по сути это поле, это - канвас """

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()


canvas = Showing()
