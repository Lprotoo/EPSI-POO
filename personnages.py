class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv

    def recevoir_degats(self, dgt):
        self.pv = self.pv - dgt
        
class Master(Personnage):
    def __init__(self, nom, pv, bonus):
        super().__init__(nom,pv)
        self.bonus = bonus
        
class Servant(Personnage):
    def __init__(self, nom, pv, att, red, mana, chance):
        super().__init__(nom,pv)
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