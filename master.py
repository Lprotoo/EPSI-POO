from personnage import *
class Servant(Personnage):
    def __init__(self, bonus):
        super().__init__()
        self.bonus = bonus
