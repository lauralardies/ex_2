class Cuenta():
    def __init__(self):
        self.dinero = 100
    
    def ver_dinero(self):
        '''
        Función que nos muestra en pantalla cuanto dinero hay en nuestra cuenta.
        '''
        return self.dinero

    def ingresar_dinero(self, ingreso):
        '''
        Acción que nos permite ingresar dinero en nuestra cuenta.
        '''
        self.dinero = self.dinero + ingreso
    
    def retierar_dinero(self, retiro):
        '''
        Acción que nos permite retirar dinero de nuestra cuenta.
        '''
        self.dinero = self.dinero - retiro
        