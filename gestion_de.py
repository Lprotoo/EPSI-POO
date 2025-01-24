import random
from slprint.slowprint import slowprint

def lancer_de(nb_faces, nb_lancers):
    """Lancer un dé avec un nombre de faces spécifié un nombre de fois donné."""
    if nb_faces <= 0:
        raise ValueError("Le nombre de faces doit être supérieur à 0.")
    if nb_lancers <= 0:
        raise ValueError("Le nombre de lancers doit être supérieur à 0.")
    lancers = [random.randint(1, nb_faces) for _ in range(nb_lancers)]
    for i, lancer in enumerate(lancers, start=1):
        slowprint(f"Lancer {i}: {lancer} \n",delay = 0.02)
        # print("\n")
    return lancers, sum(lancers)

# Exemple d'utilisation :
if __name__ == "__main__":
    lancers, total = lancer_de(2, 5)
    slowprint (f"Dégâts totaux : {total}",delay = 0.05)




