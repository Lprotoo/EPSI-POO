class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv




class Master(Personnage):
    def __init__(self,nom, pv, bonus):
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

    def __del__(self):
        print(f"\nLe servant {self.nom} est tombé au combat")
    
    def __str__(self):
        return f"{self.nom} - PV : {self.pv}, Attaque : {self.att}, Réduction de dégâts : {self.red}, Mana : {self.mana}, Chance : {self.chance}"

    def attaque(self, cible):
        dgt = self.att - cible.red
        print(f"{self.nom} attaque {cible.nom} avec une attaque faisant {dgt} de dégats")
        self.mana = self.mana + 10
        cible.pv = cible.pv - dgt

    def competence(self, cible):
        dgt = self.att - cible.red
        dgt = dgt * 1.3
        print(f"{self.nom} attaque {cible.nom} avec une attaque faisant {dgt} de dégats")
        self.mana = self.mana - 10
        cible.pv = cible.pv - dgt

    def ulti(self, cible):
        pass