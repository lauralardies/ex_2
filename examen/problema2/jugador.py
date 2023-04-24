import random

class Jugador():
    def __init__(self):
        self.dinero = 1000
    
    def seleccionar_num(self):
        return random.randint(1, 36)