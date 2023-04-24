from banca import Banca
from jugador import Jugador

banca = Banca()
contador = -1
jugadores = []

# Generamos 4 jugadores
while True:
    contador = contador + 1
    if len(jugadores) >= 4:
        break
    jugador = Jugador()
    jugadores.append(jugador)
