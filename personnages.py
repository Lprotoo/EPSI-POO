from gestion_de import lancer_de

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
        self.arte = "vide"
        self.etat = "vivant"
        

    
    def __str__(self):
        return f"{self.nom} - PV : {self.pv}, Attaque : {self.att}, Réduction de dégâts : {self.red}, Mana : {self.mana}, Chance : {self.chance}"
    
    def artefacts(self, id):
        if id == 0:
            self.arte = "anneau rouge"
            self.att += 10
            self.pv -= 5
            self.red -= 5
        elif id == 1:
            self.arte = "anneau vert"
            self.pv += 20
            self.att -= 5
        elif id == 2:
            self.arte = "anneau bleu"
            self.red += 10
            self.pv += 5
            self.att -= 10
        elif id == 3:
            self.arte = "anneau blanc"
            self.chance[1] += 5
            self.att -= 2
        elif id == 4:
            self.arte = "anneau noir"
            self.att += 20
            self.red += 20
            self.pv -= 15
            self.chance[1] -= 8
            self.compteur = 5


    def attaque(self, cible):
        if self.pv < 0:
            self.compteur -= 1
            if self.compteur == 0:
                self.pv = 50
                self.compteur = 5
            pass
        des = lancer_de(self.chance[1], self.chance[0])
        if des[1] < 20:
            multi = 0.5
            print("échec")
        elif des[1] > 45:
            multi = 1.5
            print("coup critique")
        else:
            multi = 1
            print("normal")

        dgt = (self.att * multi) - cible.red
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
