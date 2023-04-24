from cuenta import Cuenta
from contador import Contador


contador = Contador()
cuenta = Cuenta()

while True:
    contador.aumentar_contador()
    if int(contador.iteraciones()) < 60:
        cuenta.ingresar_dinero(20)
        cuenta.retierar_dinero(20)
        if int(contador.iteraciones()) < 40:
            cuenta.ingresar_dinero(100)
            cuenta.retierar_dinero(100)
            if int(contador.iteraciones()) < 20:
                cuenta.ingresar_dinero(50)
                cuenta.retierar_dinero(50)
    else:
        print('El dinero de la cuenta bancaria al comenzar es de 100€. Al terminar, tenemos ', str(cuenta.ver_dinero()), '€.')
        print('¿Coincide el dinero al principio y al final del proceso? (True/False) --> ', str(100==cuenta.ver_dinero()))
        break
