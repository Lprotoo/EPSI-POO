from slprint.slowprint import slowprint
import random
import os
from personnages import Master, Servant, Personnage

master = ["Emiya Kiritsugu", "Kotomine Kirei", "Tohsaka Tokiomi", "Matou Kariya", "Waver Velvet", "Kayneth El-Melloi Archibald", "Uryu Ryunosuke"]
servantJeu = ["Saber (Artoria Pendragon)", "Assassin (Les Hashashin)", "Archer (Gilgamesh)", "Berserker (Lancelot du Lac)", "Rider (Iskandar, Alexandre le Grand)", "Lancer (Diarmuid Ua Duibhne)", "Caster (Gilles de Rais)" ]
servantJoueur1 = []
servantStocker1 = []
servantJoueur2 = []
servantStocker2 = []

def listeFonction(liste):
    print("\n")
    for i in range(len(liste)):
        print(f"{i+1} - {liste[i]}")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

slowprint ("Bienvenue, veuillez choisir un master parmis la liste :\n", delay = 0.03, yoyo = False, vertical = False)
listeFonction(master)
masterChoix = int(input("\n >"))

slowprint (f"Bienvenue {master[masterChoix-1]}. Vous allez participez à la guerre du Saint Graal. Pour se faire, un ou plusieurs servant(s) va ou vont être invoqué pour se battre à vos cotés. Voici qui ils sont :", delay = 0.03, yoyo = False, vertical = False)
listeFonction(servantJeu)

slowprint(f"\nVeuillez choisir le nombre de servant que vous allez avoir et que vous allez affronter (max 3).", delay = 0.03, yoyo = False, vertical = False)
nombre = int(input("\n >"))

for i in range(nombre):
    servantJoueur1.append(random.choice(servantJeu))
    servantJeu.remove(servantJoueur1[i])
for i in range (nombre):
    servantJoueur2.append(random.choice(servantJeu))
    servantJeu.remove(servantJoueur2[i])

# Voici les instanciations des servants avec leur statistiques. Respectivement : pv, attaque, reduction de dégâts, mana, chance

for val in servantJoueur1:
    if val == "Saber (Artoria Pendragon)":
        Saber = Servant("Saber", 120, 90, 20, 30, "1d18")
        servantStocker1.append(Saber)
    elif val == "Assassin (Les Hashashin)":
        Assassin = Servant("Assassin",80, 60, 10, 10, "1d14")
        servantStocker1.append(Assassin)
    elif val == "Archer (Gilgamesh)":
        Archer = Servant("Archer",90, 70, 15, 10, "1d20")
        servantStocker1.append(Archer)
    elif val == "Berserker (Lancelot du Lac)":
        Berserker = Servant("Berserker",110, 70, 10, 10, "1d20")
        servantStocker1.append(Berserker)
    elif val == "Rider (Iskandar, Alexandre le Grand)":
        Rider = Servant("Rider",150, 60, 10, 30, "1d20")
        servantStocker1.append(Rider)
    elif val == "Lancer (Diarmuid Ua Duibhne)":
        Lancer = Servant("Lancer",120, 80, 15, 20, "1d20")
        servantStocker1.append(Lancer)
    elif val == "Caster (Gilles de Rais)":
        Caster = Servant("Caster",80, 60, 5, 50, "1d14")
        servantStocker1.append(Caster)

for val in servantJoueur2:
    if val == "Saber (Artoria Pendragon)":
        Saber = Servant("Saber", 120, 90, 20, 30, "1d18")
        servantStocker2.append(Saber)
    elif val == "Assassin (Les Hashashin)":
        Assassin = Servant("Assassin",80, 60, 10, 10, "1d14")
        servantStocker2.append(Assassin)
    elif val == "Archer (Gilgamesh)":
        Archer = Servant("Archer",90, 70, 15, 10, "1d20")
        servantStocker2.append(Archer)
    elif val == "Berserker (Lancelot du Lac)":
        Berserker = Servant("Berserker",110, 70, 10, 10, "1d20")
        servantStocker2.append(Berserker)
    elif val == "Rider (Iskandar, Alexandre le Grand)":
        Rider = Servant("Rider",150, 60, 10, 30, "1d20")
        servantStocker2.append(Rider)
    elif val == "Lancer (Diarmuid Ua Duibhne)":
        Lancer = Servant("Lancer",120, 80, 15, 20, "1d20")
        servantStocker2.append(Lancer)
    elif val == "Caster (Gilles de Rais)":
        Caster = Servant("Caster",80, 60, 5, 50, "1d14")
        servantStocker2.append(Caster)

slowprint(f"\nVoici les servants qui vous accompagnerons :", delay = 0.03, yoyo = False, vertical = False)
for val in servantStocker1:
    print(f"\n {val}")
          
slowprint(f"\nEt voici les servants qui vous affronteront :", delay = 0.03, yoyo = False, vertical = False)
for val in servantStocker2:
    print(f"\n {val}")

# Test fonction combat
clear_terminal()

def combat(attaquant, cibles):
    actions = ["attaque normale", "attaque spéciale (coute 10 de mana)"]
    slowprint(f"\nC'est au tour de {attaquant.nom} d'attaquer ", delay = 0.03, yoyo = False, vertical = False)
    print(f"\npv : {attaquant.pv} attaque : {attaquant.att} mana : {attaquant.mana}")
    listeFonction(actions)
    choix1 = int(input("\n >"))
    slowprint(f"\nChoisissez qui vous voulez attaquer", delay = 0.03, yoyo = False, vertical = False)
    for val in cibles:
        print(f"\n {val.nom}")
    choix2 = int(input("\n >"))
    if choix1 == 1:
        attaquant.attaque(cibles[choix2-1])
    elif choix1 == 2:
        if attaquant.mana > 10:
            attaquant.competence(cibles[choix2-1])
        else:
            print("vous n'avez pas assez de mana, l'attaque échoue")
    if cibles[choix2-1].pv <= 0:
        pass
    

    

nb_tours = 0

def tour():
    global nb_tours
    nb_tours += 1
    print(f"c'est le tour {nb_tours}")
    if nombre == 3:
        combat(servantStocker1[0], servantStocker2)
        combat(servantStocker2[0], servantStocker1)
        combat(servantStocker1[1], servantStocker2)
        combat(servantStocker2[1], servantStocker1)
        combat(servantStocker1[2], servantStocker2)
        combat(servantStocker2[2], servantStocker1)
    elif nombre ==2:
        combat(servantStocker1[0], servantStocker2)
        combat(servantStocker2[0], servantStocker1)
        combat(servantStocker1[1], servantStocker2)
        combat(servantStocker2[1], servantStocker1)
    else:
        combat(servantStocker1[0], servantStocker2)
        combat(servantStocker2[0], servantStocker1)
    

    

tour()
tour()



#Tests
#print(servantStocker2[0].pv)
#print(servantStocker2[1].pv)
#servantStocker1[0].attaque(servantStocker2[0])
#servantStocker1[1].competence(servantStocker2[1])
#print(servantStocker2[0].pv)
#print(servantStocker2[1].pv)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Appuyez sur Entrée pour passer au résumé du combat : ")
input()
clear_terminal()









