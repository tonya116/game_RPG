# -*- coding: utf-8 -*-

from config import *
import sys
from showing import *
import subprocess
import generate_all as ga
import socket




class Menu():


    def __init__(self):


        self.pause_F = Frame(canvas.root)
        self.menu_F = Frame(canvas.root)


        self.resume = Button(self.pause_F, text="resume", background = "#555", command=lambda x="resume":self.single_bar(x))
        self.save = Button(self.pause_F, text="save", background = "#555",command=self.saving_game)
        self.exit = Button(self.pause_F, text="exit", background = "#555",command=self.menu_bar)


        self.single = Button(self.menu_F, text="single", background = "#555", command=lambda x="":self.single_bar(x))
        self.multiplayer = Button(self.menu_F, text="multiplayer", background = "#555", command=self.multiplayer_bar)
        self.quit = Button(self.menu_F, text="quit", background = "#555", command=sys.exit)

        self.resume.grid( pady = 10, padx = 10)
        self.save.grid( pady = 10, padx = 10)
        self.exit.grid( pady = 10, padx = 10)




        self.single.grid(row = 2, column = 0, pady = 10, padx = 10)
        self.multiplayer.grid(row = 4, column = 0, pady = 10, padx = 10)
        self.quit.grid(row = 6, column = 0, pady = 10, padx = 10)

        self.menu_F.grid()

        canvas.root.bind("<Escape>", self.pause_bar)


    def single_bar(self, event):

        if event == "resume":
            canvas.canvas.grid(row = 3, column = 2)
            self.menu_F.grid_remove()
            self.pause_F.grid_remove()
        else:
            ga.regenerate()
            canvas.canvas.grid(row = 3, column = 2)
            self.menu_F.grid_remove()
            self.pause_F.grid_remove()


    def pause_bar(self, event):

        canvas.canvas.grid_remove()

        self.menu_F.grid_remove()
        self.pause_F.grid()

    def menu_bar(self):
        self.menu_F.grid()
        canvas.canvas.grid_remove()
        self.pause_F.grid_remove()


    def multiplayer_bar(self):

        s = socket.socket()
        s.connect(("127.0.0.1", port))


        print("Enter your name:")
        data = bytes(input(), encoding = "utf-8")



        canvas.canvas.grid(row = 3, column = 2)
        self.menu_F.grid_remove()
        self.pause_F.grid_remove()



        s.send(data)

        d = s.recv(1024)


        print(d)



    def saving_game(self):
        pass


menu = Menu()



#menu.menu_F.mainloop()








"""
fdhdf

        self.multiplayer_game.grid( pady = 10, padx = 10)
        self.quit.grid( pady = 10, padx = 10)
        self.save = Button(self.pause, text="save", background = "#555",command=self.saving_game)
                self.multiplayer_game = Button(self.menu, text="multiplayer", background = "#555",command=self.multiplayer)
                self.quit = Button(self.menu, text="quit", background = "#555",command=sys.exit)

    asdfg
    """
