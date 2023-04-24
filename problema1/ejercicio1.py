from cuenta import Cuenta
from contador import Contador

contador = Contador()
cuenta = Cuenta()
paso = 1

while True:
    contador.aumentar_contador()
    if paso == 1:
        if contador.iteraciones() != 40: # Primero queremos 40 procesos que ingresen 100€
            cuenta.ingresar_dinero(100)
        else: # Significa que ya hemos hecho 40 iteraciones
            contador = Contador() # Reiniciamos el contador
            paso = paso + 1 # Vamos al siguiente paso
    elif paso == 2:
        if contador.iteraciones() != 20: # Segundo, queremos 20 procesos que ingresen 50€
            cuenta.ingresar_dinero(50)
        else: # Significa que ya hemos hecho 20 iteraciones
            contador = Contador() # Reiniciamos el contador
            paso = paso + 1 # Vamos al siguiente paso
    elif paso == 3:
        if contador.iteraciones() != 60: # Tercero, queremos 60 procesos que ingresen 20€
            cuenta.ingresar_dinero(20)
        else: # Significa que ya hemos hecho 60 iteraciones
            contador = Contador() # Reiniciamos el contador
            paso = paso + 1 # Vamos al siguiente paso
    elif paso == 4:
        if contador.iteraciones() != 40: # Luego, queremos 40 procesos que retiren 100€
            cuenta.retierar_dinero(100)
        else: # Significa que ya hemos hecho 40 iteraciones
            contador = Contador() # Reiniciamos el contador
            paso = paso + 1 # Vamos al siguiente paso
    elif paso == 5:
        if contador.iteraciones() != 20: # Seguidamente, queremos 20 procesos que retiren 50€
            cuenta.retierar_dinero(50)
        else: # Significa que ya hemos hecho 20 iteraciones
            contador = Contador() # Reiniciamos el contador
            paso = paso + 1 # Vamos al siguiente paso
    elif paso == 6:
        if contador.iteraciones() != 60: # Por último, queremos 60 procesos que retiren 20€
            cuenta.retierar_dinero(20)
        else: # Significa que ya hemos hecho 60 iteraciones
            contador = Contador() # Reiniciamos el contador
            paso = paso + 1 # Vamos al siguiente paso
    else:
        print('El dinero de la cuenta bancaria al comenzar es de 100€. Al terminar, tenemos ', str(cuenta.ver_dinero()))
        print('¿Coincide el dinero al principio y al final del proceso? (True/False) ', str(100==cuenta.ver_dinero()))
        break
