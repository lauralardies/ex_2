import random

class Banca():
    def __init__(self):
        self.dinero = 50000

    def num_azar(self):
        return random.randint(0, 36)
