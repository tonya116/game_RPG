import showing

class Humans():


    def __init__(self, age, name, race, health, force, stamina, iq, magic, money ):
        self.age = age
        self.name = name
        self.race = race
        self.health = health
        self.force = force
        self.stamina = stamina
        self.iq = iq
        self.magic = magic
        self.level_health = self.health
        self.level_force = 100
        self.level_stamina = 100
        self.level_iq = 100
        self.level_magic = 100
        self.money = money


    def show(self):
        showing.Showing().show()

    def damage(self, damage):
        self.level_health -= damage

    def upgrade_force(self):
        self.force += 1

    def upgrade_stamina(self):
        self.stamina += 1

    def upgrade_iq(self):
        self.iq += 1

    def upgrade_magic(self):
        self.magic += 1

    def regeneration(self):
        if self.level_health <= self.health-10:
            self.level_magic -= self.level_magic/2
            self.level_health += int(0.1 * self.health)
