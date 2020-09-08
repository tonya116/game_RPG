

from config import *
from random import randrange as rndt
import showing as sh


import portal
import barrier
import spike_pillar as sp
import generate_all as ga


class Interaction():


    def portal(self, entity):

        entity.coords()
        for item in ga.list_of_portals:
            if entity.coordinates == item.coordinates:
                range = 50
                x = rndt(-range, range, step)
                y = rndt(-range, range, step)
                while (entity.coordinates[0] + x < 0 or entity.coordinates[2] + x > WIDTH) or (entity.coordinates[1] + y < 0 or entity.coordinates[3] + y > HEIGHT):
                    x = rndt(-range, range, step)
                    y = rndt(-range, range, step)
                sh.canvas.canvas.move(entity.rect_id.rect_id, x, y)
    def barrier(self, entity):

        entity.coords()
        self.word = 0


        for item in barrier.list_of_barriers:
            if (entity.x1 == 0 and entity.v_x == -step and (entity.v_y == step or entity.v_y == -step) ) or  (entity.y1 == 0 and entity.v_y == -step and (entity.v_x == step or entity.v_x == -step)) or (entity.x2 == WIDTH and entity.v_x == step ) or (entity.y2 == HEIGHT and entity.v_y == step ) or (entity.x1 == item.coordinates[2] and entity.y1 == item.coordinates[1] and entity.v_x == -step and entity.v_y == 0) or (entity.x1 == item.coordinates[0] and entity.y1 == item.coordinates[3] and entity.v_x == 0 and entity.v_y == -step) or (entity.y1 == item.coordinates[1] and entity.x2 == item.coordinates[0] and entity.v_x == step and entity.v_y == 0) or (entity.x1 == item.coordinates[0] and entity.y2 == item.coordinates[1] and entity.v_x == 0 and entity.v_y== step):
                pass
            else:
                self.word += 1

        if self.word == len(barrier.list_of_barriers):
            sh.canvas.canvas.move(entity.rect_id.rect_id, entity.v_x, entity.v_y)

        self.word = 0

    def pillares(self, entity):
        entity.coords()
        for i in ga.list_of_pillares:
            #укалывание справа
            if  entity.x1 == i.coordinates[2] and entity.y1 == i.coordinates[1] :
                entity.damage(i.force)
                entity.rect_id.move(step, 0)
            #укалывание снизу
            elif entity.x1 == i.coordinates[0] and entity.y1 == i.coordinates[3] :
                entity.damage(i.force)
                entity.rect_id.move(0, step)
            #укалывание слева
            elif entity.y1 == i.coordinates[1] and entity.x2 == i.coordinates[0] :
                entity.damage(i.force)
                entity.rect_id.move(-step, 0)
            #укалывание сверху
            elif entity.x1 == i.coordinates[0] and entity.y2 == i.coordinates[1] :
                entity.damage(i.force)
                entity.rect_id.move(0, -step)

    def apple(self, entity):
        entity.coords()
        for i in ga.list_of_apples:

            if entity.coordinates[0] == i.coordinates[0] and entity.coordinates[1] == i.coordinates[1]:
                if entity.race == "Hero":
                    entity.healing(i.force)
                    i.death()
                elif entity.race == "org":
                    entity.damage(i.force)
                    i.death()


    def orgs(self, entity, item):
        entity.coords()

        for i in item:
            if entity.coordinates[0] == i.coordinates[0] and entity.coordinates[1] == i.coordinates[1]:
                i.damage(entity.force)





inter = Interaction()
