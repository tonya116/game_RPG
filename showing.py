from tkinter import *



root = Tk()
root.geometry("500x500")



canvas = Canvas(root, width = 500, height = 500, bg = 'black')

class Showing:
    def __init__(self):
        pass



    def moving(self):
        pass


canvas.pack()
root.mainloop()


'''

global person
if event.char == "s":

    canvas.coords(person, +10,+10,+10,+10)
print("yes")
print(event.char)


canvas.bind("<Key>", moving)

person = canvas.create_rectangle(10, 10, 20, 20, fill = "green")
'''
