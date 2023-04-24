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
    
    def par_impar(self, predicciones):
        resultados = []
        if self.num_azar % 2 == 0:
            solucion = 'Par'
        else:
            solucion = 'Impar'
        for prediccion in predicciones:
            if prediccion == solucion:
                resultados.append(True)
            else:
                resultados.append(False)
        return resultados