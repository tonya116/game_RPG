import showing as sh
import hero
import portal as prtl
import orgs

from random import randrange as rndt


class Checker_collide():

    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def show_info(self):
        pass


    def interaction(self):
        if self.item1 != self.item2:
            self.show_info()
