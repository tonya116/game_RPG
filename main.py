## -*- coding: utf-8 -*-
import humans
import showing as sh
import spike_pillar as sp




hero = humans.Humans("Den", "Hero", 100, 100, 150, 200)
hero.move_hero()

sp1 = sp.SpikePillar("1", "spike_pillar", 100, 100, 350, 200)

list_of_coords = [ {sp1.x, sp1.y} ]

hero.collide_checker(list_of_coords)


sh.canvas.root.mainloop()
