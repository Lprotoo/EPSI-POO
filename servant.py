from personnage import *

class Servant(Personnage):
    def __init__(self, pv, att, red, mana, chance):
        super().__init__()
        self.pv = pv
        self.att = att
        self.red = red
        self.mana = mana
        self.chance = chance
    
    def attaque1(self, cible):
        pass
    
    def attaque2(self, cible):
        pass

    def ulti(self, cible):
        pass

