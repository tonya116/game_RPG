# -*- coding: utf-8 -*-
import humans
import showing as sh
import spike_pillar as sp


list_of_objects = []
list_of_objects.append(humans.hero)
list_of_objects.append(sp.sp1)



def collide_checker():
    for i in list_of_objects:
        i.coords()
    if humans.hero.coordinates == sp.sp1.coordinates:
        humans.hero.damage(10)
        print(humans.hero.health)
    sh.canvas.root.after(1000, collide_checker)

collide_checker()

sh.canvas.root.mainloop()
