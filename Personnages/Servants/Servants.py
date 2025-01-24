import sys
import os
# Ajoutez dynamiquement le chemin du répertoire racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from personnage import *

class Servant(Personnage):
    def __init__(self, att, attspe, res, resspe, reduc, augment, garde, esquive):
        super().__init__()
        self.att = att
        self.attspe = attspe
        self.res = res
        self.resspe = resspe
        self.reduc = reduc
        self.augment = augment
        self.garde = garde
        self.esquive = esquive

    