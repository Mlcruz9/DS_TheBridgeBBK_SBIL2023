import functions

print("Bienvenido al juego de Hundir la flota!")
nombre = input("Introduce tu nombre!: ")
tablero = functions.init_tablero(fill= " ")

functions.barco_aleatorio(4, tablero=tablero)

print("Inicia el juego!")

functions.disparo(tablero=tablero, maq= False)

