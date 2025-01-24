import sys
import os
# Ajoutez dynamiquement le chemin du répertoire racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from personnage import *


class Servant(Personnage):
    def __init__(self):
        super().__init__()
