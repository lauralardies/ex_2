import random

class Jugador():
    def __init__(self):
        self.dinero = 1000
        self.par_impar = ['Par', 'Impar']
    
    def seleccionar_num(self):
        return random.randint(1, 36)

    def seleccionar_palabra(self):
        return random.choice(self.par_impar)

    def restar_dinero(self, resta):
        self.dinero = self.dinero - resta        
    
    def ganar_dinero(self, suma):
        self.dinero = self.dinero + suma