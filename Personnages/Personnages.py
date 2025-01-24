class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv

    def recevoir_degats(self, dgt):
        self.pv = self.pv - dgt

    
