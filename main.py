from slprint.slowprint import slowprint
import random
from random import randint
import os
from personnages import Master, Servant, Personnage
from gestion_de import lancer_de

lmaster = ["Emiya Kiritsugu", "Kotomine Kirei", "Tohsaka Tokiomi", "Matou Kariya", "Waver Velvet", "Kayneth El-Melloi Archibald", "Uryu Ryunosuke"]
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

slowprint ("Bienvenue, veuillez choisir un master parmis la liste :\n", delay = 0.01, yoyo = False, vertical = False)
listeFonction(lmaster)
mchoix = input("\n >")
if mchoix == "1" or mchoix == "2" or mchoix == "3" or mchoix == "4" or mchoix == "5" or mchoix == "6" or mchoix == "7": # Gestion des erreurs
    mchoix = int(mchoix)
else:
    mchoix = 1



# Vérifie que le choix est valide
if 1 <= mchoix <= len(lmaster):
    if mchoix == 1:
        master = Master(lmaster[0],100, 1)
    elif mchoix == 2:
        master = Master(lmaster[1],100, 2)
    elif mchoix == 3:
        master = Master(lmaster[2],100, 3)
    elif mchoix == 4:
        master = Master(lmaster[3],100, 4)
    elif mchoix == 5:
        master = Master(lmaster[4],100, 5)
    elif mchoix == 6:
        master = Master(lmaster[5],100, 6)
    elif mchoix == 7:
        master = Master(lmaster[6],100, 7)

else:
    print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")

mchoix2 = randint(0, 6)


if mchoix == mchoix2:
    mchoix2 += 1
if mchoix2 == 1:
    master2 = Master(lmaster[0],100, 1)
elif mchoix2 == 2:
    master2 = Master(lmaster[1],100, 2)
elif mchoix2 == 3:
    master2 = Master(lmaster[2],100, 3)
elif mchoix2 == 4:
    master2 = Master(lmaster[3],100, 4)
elif mchoix2 == 5:
    master2 = Master(lmaster[4],100, 5)
elif mchoix2 == 6:
    master2 = Master(lmaster[5],100, 6)
elif mchoix2 == 7:
    master2 = Master(lmaster[6],100, 7)
elif mchoix2 == 8:
    master2 = Master(lmaster[0],100, 1)



slowprint (f"Bienvenue {master.nom}. Vous allez participez à la guerre du Saint Graal. Pour se faire, un ou plusieurs servant(s) va ou vont être invoqué pour se battre à vos cotés. Voici qui ils sont :", delay = 0.01, yoyo = False, vertical = False)
listeFonction(servantJeu)

slowprint(f"\nVous allez affronter {master2.nom}", delay = 0.01, yoyo = False, vertical = False)



slowprint(f"\nVeuillez choisir le nombre de servant que vous allez avoir et que vous allez affronter (max 3).", delay = 0.01, yoyo = False, vertical = False)
nombre = input("\n >")
if nombre == "1" or nombre == "2" or nombre == "3":
    nombre = int(nombre)
else:
    nombre = 1

for i in range(nombre):
    servantJoueur1.append(random.choice(servantJeu))
    servantJeu.remove(servantJoueur1[i])
for i in range (nombre):
    servantJoueur2.append(random.choice(servantJeu))
    servantJeu.remove(servantJoueur2[i])



for val in servantJoueur1:
    if val == "Saber (Artoria Pendragon)":
        Saber = Servant("Saber", 120, 90, 20, 30, [3, 18])
        servantStocker1.append(Saber)
    elif val == "Assassin (Les Hashashin)":
        Assassin = Servant("Assassin",80, 60, 10, 10, [3, 21])
        servantStocker1.append(Assassin)
    elif val == "Archer (Gilgamesh)":
        Archer = Servant("Archer",90, 70, 15, 10, [3, 17])
        servantStocker1.append(Archer)
    elif val == "Berserker (Lancelot du Lac)":
        Berserker = Servant("Berserker",110, 70, 10, 10, [3, 16])
        servantStocker1.append(Berserker)
    elif val == "Rider (Iskandar, Alexandre le Grand)":
        Rider = Servant("Rider",150, 60, 10, 30, [3, 17])
        servantStocker1.append(Rider)
    elif val == "Lancer (Diarmuid Ua Duibhne)":
        Lancer = Servant("Lancer",120, 80, 15, 20, [3, 15])
        servantStocker1.append(Lancer)
    elif val == "Caster (Gilles de Rais)":
        Caster = Servant("Caster",80, 60, 5, 50, [3, 19])
        servantStocker1.append(Caster)

for val in servantJoueur2:
    if val == "Saber (Artoria Pendragon)":
        Saber = Servant("Saber", 120, 90, 20, 30, [3, 18])
        servantStocker2.append(Saber)
    elif val == "Assassin (Les Hashashin)":
        Assassin = Servant("Assassin",80, 60, 10, 10, [3, 21])
        servantStocker2.append(Assassin)
    elif val == "Archer (Gilgamesh)":
        Archer = Servant("Archer",90, 70, 15, 10, [3, 17])
        servantStocker2.append(Archer)
    elif val == "Berserker (Lancelot du Lac)":
        Berserker = Servant("Berserker",110, 70, 10, 10, [3, 16])
        servantStocker2.append(Berserker)
    elif val == "Rider (Iskandar, Alexandre le Grand)":
        Rider = Servant("Rider",150, 60, 10, 30, [3, 17])
        servantStocker2.append(Rider)
    elif val == "Lancer (Diarmuid Ua Duibhne)":
        Lancer = Servant("Lancer",120, 80, 15, 20, [3, 15])
        servantStocker2.append(Lancer)
    elif val == "Caster (Gilles de Rais)":
        Caster = Servant("Caster",80, 60, 5, 50, [3, 19])
        servantStocker2.append(Caster)


clear_terminal()


listearte = ["anneau rouge : attaque + 10 | pv - 5 | défense -5", "anneau vert : pv + 20 | attaque -5", "anneau bleu : défense + 10 | pv + 5 | attaque -5 ", "anneau blanc : chance + 5 | attaque -2", "anneau noir : attaque + 20 | défense + 20 | pv - 15 | chance -8"]
listeFonction(listearte)
for val in servantStocker1:
    slowprint(f"\nChoississez un artefact pour {val.nom} :", delay = 0.01, yoyo = False, vertical = False)
    choixarte = input()
    if choixarte == "1" or choixarte == "2" or choixarte == "3" or choixarte == "4" or choixarte == "5":
        choixarte = int(choixarte) - 1
    else:
        choixarte = randint(0, 4)
    val.artefacts(choixarte)
    
clear_terminal()

slowprint(f"\nVoici le ou les servants qui vous accompagnerons :", delay = 0.01, yoyo = False, vertical = False)
for val in servantStocker1:
    print(f"\n {val}")

print("\nAppuyez sur entrée pour continuer")
input()

          
slowprint(f"\nEt voici le ou les servants qui vous affronteront :", delay = 0.01, yoyo = False, vertical = False)
for val in servantStocker2:
    val.artefacts(randint(0, 4))
    print(f"\n {val}")


print("\nAppuyez sur entrée pour continuer")
input()


clear_terminal()

def combat(attaquant, cibles):
    if attaquant.pv > 0:
        actions = ["attaque normale", "attaque spéciale (coute 20 de mana)", "attaque ultime (coute 50 de mana)"]
        slowprint(f"\nC'est au tour de {attaquant.nom} d'attaquer ", delay = 0.03, yoyo = False, vertical = False)
        print(f"\npv : {attaquant.pv} | attaque : {attaquant.att} | mana : {attaquant.mana} | artéfact : {attaquant.arte}")
        listeFonction(actions)
        print(f"\nvos pv : {master.pv} | pv du master adverse : {master2.pv}")
        choix1 = input("\n >")
        if choix1 == "1" or choix1 == "2" or choix1 == "3": # Gestion erreur
            choix1 = int(choix1)
        else: 
            choix1 = 1
        slowprint(f"\nChoisissez qui vous voulez attaquer", delay = 0.03, yoyo = False, vertical = False)
        for val in cibles:
            print(f"\n {val.nom} | pv : {val.pv}")
        choix2 = input("\n >")
        if len(cibles) == 1: # Gestion erreur
            if choix2 == "1":
                choix2 = int(choix2)
            else:
                choix2 = 1
        elif len(cibles) == 2:
            if choix2 == "1" or choix2 == "2":
                choix2 = int(choix2)
            else:
                choix2 = 1    
        elif len(cibles) == 3:
            if choix2 == "1" or choix2 == "2" or choix2 == "3":
                choix2 = int(choix2)
            else:
                choix2 = 1          

        if choix1 == 1:
            attaquant.attaque(cibles[choix2-1])
        elif choix1 == 2:
            if attaquant.mana > 20:
                attaquant.competence(cibles[choix2-1])
            else:
                print("vous n'avez pas assez de mana, l'attaque échoue")
        elif choix1 == 3:
            attaquant.ulti(cibles[choix2-1])
        if cibles[choix2-1].pv <= 0:
            print(f"le servant {cibles[choix2-1].nom} est tombé au combat, vous allez donc attaquer une fois le master adverse")
            input()
            if cibles == servantStocker2:
                attaquant.attaquemaster(master2)
            else:
                attaquant.attaquemaster(master)
            cibles[choix2-1].pv = 75 #On ressucite le servant
    else:
        pass


    

    

nb_tours = 0

def tour():
    global nb_tours
    nb_tours += 1
    print(f"c'est le tour {nb_tours}")
    if nombre == 3:
        combat(servantStocker1[0], servantStocker2)
        boucle()
        combat(servantStocker2[0], servantStocker1)
        boucle()
        combat(servantStocker1[1], servantStocker2)
        boucle()
        combat(servantStocker2[1], servantStocker1)
        boucle()
        combat(servantStocker1[2], servantStocker2)
        boucle()
        combat(servantStocker2[2], servantStocker1)
        boucle()
    elif nombre ==2:
        combat(servantStocker1[0], servantStocker2)
        boucle()
        combat(servantStocker2[0], servantStocker1)
        boucle()
        combat(servantStocker1[1], servantStocker2)
        boucle()
        combat(servantStocker2[1], servantStocker1)
        boucle()
    else:
        combat(servantStocker1[0], servantStocker2)
        boucle()
        combat(servantStocker2[0], servantStocker1)
        boucle()




def boucle():
    if master.pv <= 0:
        slowprint(f"\nLe master {master2.nom} a remporté le combat", delay = 0.03, yoyo = False, vertical = False)
        input()
        exit()
        return 0
    elif master2.pv <= 0:
        slowprint(f"\nLe master {master.nom} a remporté le combat", delay = 0.03, yoyo = False, vertical = False)
        input()
        exit()
        return 0
    else:
        return 1



while boucle() == 1:
    tour()





#Tests
#print(servantStocker2[0].pv)
#print(servantStocker2[1].pv)
#servantStocker1[0].attaque(servantStocker2[0])
#servantStocker1[1].competence(servantStocker2[1])
#print(servantStocker2[0].pv)
#print(servantStocker2[1].pv)














