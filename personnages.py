from gestion_de import lancer_de
import random

class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv




class Master(Personnage):
    def __init__(self,nom, pv, idbonus):
        super().__init__(nom,pv)
        self.idbonus = idbonus #non utilisé car pas d'idée

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
            self.etat = "mort"
        else:
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


    def attaquemaster(self, cible):
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

        dgt = self.att * multi
        print(f"{self.nom} attaque {cible.nom} avec une attaque faisant {dgt} de dégats")
        cible.pv = cible.pv - dgt

    def competence(self, cible):
        dgt = self.att - cible.red
        dgt = dgt * 1.3
        print(f"{self.nom} attaque {cible.nom} avec une attaque faisant {dgt} de dégats")
        self.mana = self.mana - 10
        cible.pv = cible.pv - dgt

    def ulti(self, cible):
        if self.mana >= 50:
            self.mana -= 50
            if self.nom == "Saber":
                dgt = random.randint(120, 160)
                print(f"{self.nom} utilise Excalibur et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.att -= 15  # Réduction de l'attaque de l'ennemi
                print(f"{cible.nom} est affaibli : -15 attaque.")

            elif self.nom == "Assassin":
                dgt = random.randint(110, 150)
                print(f"{self.nom} utilise Tsubame Gaeshi et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.red -= 10  # Réduction de la réduction de dégâts de l'ennemi
                print(f"{cible.nom} est affaibli : -10 réduction de dégâts.")

            elif self.nom == "Archer":
                dgt = random.randint(100, 140)
                print(f"{self.nom} utilise Unlimited Blade Works et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.chance[1] -= 10  # Réduction de la chance de l'ennemi
                print(f"{cible.nom} est affaibli : -10 chance.")

            elif self.nom == "Berserker":
                dgt = random.randint(130, 170)
                print(f"{self.nom} utilise God Hand et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.pv -= 20  # Réduction supplémentaire des PV de l'ennemi
                print(f"{cible.nom} est affaibli : -20 PV supplémentaires.")

            elif self.nom == "Rider":
                dgt = random.randint(110, 150)
                print(f"{self.nom} utilise Ionioi Hetairoi et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.att -= 10  # Réduction de l'attaque de l'ennemi
                cible.red -= 5  # Réduction de la réduction de dégâts de l'ennemi
                print(f"{cible.nom} est affaibli : -10 attaque, -5 réduction de dégâts.")

            elif self.nom == "Lancer":
                dgt = random.randint(120, 160)
                print(f"{self.nom} utilise Gae Bolg et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.chance[1] -= 15  # Réduction de la chance de l'ennemi
                print(f"{cible.nom} est affaibli : -15 chance.")

            elif self.nom == "Caster":
                dgt = random.randint(100, 140)
                print(f"{self.nom} utilise Rule Breaker et inflige {dgt} dégâts à {cible.nom}!")
                cible.pv -= dgt
                cible.mana -= 20  # Réduction du mana de l'ennemi
                print(f"{cible.nom} est affaibli : -20 mana.")

            else:
                print(f"{self.nom} n'a pas d'ultime défini.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour utiliser son ultime.")
