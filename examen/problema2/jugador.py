import random

class Jugador():
    def __init__(self):
        self.dinero = 1000
    
    def seleccionar_num(self):
        return random.randint(1, 36)

    def restar_dinero(self, resta):
        self.dinero = self.dinero - resta        
    
    def ganar_dinero(self, suma):
        self.dinero = self.dinero + suma