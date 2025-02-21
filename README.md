# Liens : 

Trello : https://trello.com/invite/b/67934db6a62ab1f8a3c3c15c/ATTIc7f2f2249566cdd80185371a04e2d64851AA7B50/poo-fate-python (si il expire redemandez le à Liam(lproto sur discord))

github : https://github.com/Lprotoo/EPSI-POO

# Pour lancer le script :

Installer le module de slowprint :  pip install slprint11-pkg

## Etape 1 : Initialisation des personnages

Le script vous demande de choisir un master parmi une liste, il faut choisir un chiffre entre 1 et 7.

Ensuite Le programme vous demande de choisir combien de servant vont combattre (entre 1 et 3) par exemple si vous choisissez 3 le combat opposera 1 master et 3 servant
contre un autre master et 3 servant.

Après cela le programme demande de choisir pour chaque servant dans notre équipe un artefact, il y en a 5 en tout et chacun donne un bonus de stats.
Les artefacts de l'équipe ennemie sont choisi aléatoirement.

## Etape 2 : Combat

Lors du combat, l'odre d'attaque est défini aléatoirement quand les servants sont créés,
Vous avez le choix entre 3 actions :
- Faire une attaque normale qui utilise un jet de dé basé sur la chance du servant, faire une attaque normale augmente le mana de l'attaquant de 5.
- Faire une attaque spéciale qui coute 20 de mana qui va infliger des dégâts non soumit à l'aléatoire et qui va soigner 10 pv et augmenter l'attaque de 5.
- Faire une attaque ultime qui coute 50 de mana qui a un effet spécial en fonction du servant qui la lance.



## Fonctionalité supplémentaire :

Notre fonctionalité supplémenaire est la gestion entre servant et master, Quand un servant meurt, le servant qui l'a tué peut porter une attaque normale au master adverse, chaque master possède 100 pv et si un des 2 master tombe à 0 pv le combat se fini. Le servant mort ressucite une fois le tour fini avec 75 pv.
