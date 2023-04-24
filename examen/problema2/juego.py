import random 

class Juego():
    def __init__(self):
        self.num_azar = random.randint(0, 36)
    
    def num_concreto(self, predicciones):
        resultados = []
        for prediccion in predicciones:
            if prediccion == self.num_azar:
                resultados.append(True)
            else:
                resultados.append(False)
        return resultados
