# -*- coding: utf-8 -*-
from random import randrange as rndt
import humans
import showing as sh
import spike_pillar as sp
import portal as prtl


list_of_objects = []
list_of_objects.append(humans.hero)
list_of_objects.append(sp.sp1)
list_of_objects.append(prtl.p1)



def collide_checker():
    for i in list_of_objects:
        i.coords()
    if list_of_objects[0].coordinates ==  list_of_objects[2].coordinates:
        sh.canvas.canvas.move(humans.hero.rect_id, rndt(-100, 100, 10),rndt(-100, 100, 10))
    sh.canvas.root.after(10, collide_checker)

collide_checker()

sh.canvas.root.mainloop()
