class Contador():
    def __init__(self):
        self.contador = -1
    
    def iteraciones(self):
        return self.contador
    
    def aumentar_contador(self):
        self.contador = self.contador + 1
