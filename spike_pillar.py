# -*- coding: utf-8 -*-
import showing as sh

class SpikePillar:
    """
    этот класс связан со всем, что связано с шипованным столбом
    """
    def __init__(self, name, race, health, force, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.race = race
        self.force = force
        self.color = "gray"
        self.rect_id = sh.canvas.canvas.create_rectangle(self.x,
                                                         self.y,
                                                         self.x + 10,
                                                         self.y + 10,
                                                         fill=self.color)

    def coords(self):
        self.coordinates = sh.canvas.canvas.coords(self.rect_id)




sp1 = SpikePillar("1", "spike_pillar", 100, 100, 350, 200)
sp1.coords()
