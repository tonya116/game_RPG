class Orgs():


    def __init__(self, age, name, race, health, force, stamina, iq, magic, money ):
        self.age = age
        self.name = name
        self.race = race
        self.health = health
        self.force = force
        self.stamina = stamina
        self.iq = iq
        self.magic = magic
        self.money = money
    def upgrade_force(self):
        self.force += 1

    def upgrade_stamina(self):
        self.stamina += 1

    def upgrade_iq(self):
        self.iq += 1

    def upgrade_magic(self):
        self.magic += 1
