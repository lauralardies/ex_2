from banca import Banca
from jugador import Jugador
from juego import Juego

banca = Banca()
contador = -1
jugadores = []
predicciones = []

# Generamos 4 jugadores
while True:
    contador = contador + 1
    if len(jugadores) >= 4:
        break
    jugador = Jugador()
    jugadores.append(jugador)

# Creamos predicciones
while True:
    # Comenzamos a jugar
    print('A qué juego quieres jugar? Selecciona un número del 1 al 4.')
    print('1. Número al azar.')
    print('2. Par / Impar.')
    print('3. Martingala.')
    print('4. Exit.')
    seleccion = input('>> ')

    if seleccion == '1':
        for jugador in jugadores:
            predicciones.append(int(jugador.seleccionar_num()))
            jugador.restar_dinero(10)

        resultados = Juego().num_concreto(predicciones)
        for resultado in resultados:
            for jugador in jugadores:
                if resultado == True:
                    jugador.ganar_dinero(360)
                else:
                    banca.ganar_dinero(10)

        print('¿Quieres seguir jugando? ([Si] / No)')
        decision = input('>> ')
        if decision == 'No':
            print('Hasta luego!')
            break
    
    elif seleccion == '2':
        for jugador in jugadores:
            predicciones.append(jugador.seleccionar_palabra())
            jugador.restar_dinero(10)

        resultados = Juego().par_impar(predicciones)
        for resultado in resultados:
            for jugador in jugadores:
                if resultado == True:
                    jugador.ganar_dinero(20)
                else:
                    banca.ganar_dinero(10)

        print('¿Quieres seguir jugando? ([Si] / No)')
        decision = input('>> ')
        if decision == 'No':
            print('Hasta luego!')
            break
    
    elif seleccion == '3':
        print('No está hecho.')
        print('¿Quieres seguir jugando? ([Si] / No)')
        decision = input('>> ')
        if decision == 'No':
            print('Hasta luego!')
            break
    
    elif seleccion == '4':
        print('Hasta luego!')
        break
    
    else:
        print('No ha seleccionado una opción correcta. Inténtelo de nuevo.')