import numpy as np

def init_tablero(fill, maquina_oc = False):

    if maquina_oc:
        tablero = np.full((10, 10), fill)
    
    else:
        tablero = np.full((10, 10), fill)

    return tablero

def disparo(tablero, maq = True):

    if maq:
        coord_x = int(input('Introduzca coordenada x:'))
        coord_y = int(input('Introduzca coordenada y:'))

        if tablero[coord_x, coord_y] == "O":
            tablero[coord_x, coord_y] = "X"
            TABLERO_OCULTO[coord_x, coord_y] = "X"
            print("Has acertado!")
            print(TABLERO_OCULTO)

        elif tablero[coord_x, coord_y] == " ":
            tablero[coord_x, coord_y] = "-"
            TABLERO_OCULTO[coord_x, coord_y] = "-"
            print("Has fallado!")
            print(TABLERO_OCULTO)
            
        elif tablero[coord_x, coord_y] == "X":
            print("Disparo previamente realizado!")
            print(TABLERO_OCULTO)

        elif tablero[coord_x, coord_y] == "-":
            print("Disparo previamente realizado!")
            print(TABLERO_OCULTO)
    
    else:
        coord_x = np.random.randint(0, 10)
        coord_y = np.random.randint(0, 10)

        if tablero[coord_x, coord_y] == "O":
            tablero[coord_x, coord_y] = "X"
            TABLERO_OCULTO[coord_x, coord_y] = "X"
            print("Has acertado!")
            print(tablero)

        elif tablero[coord_x, coord_y] == " ":
            tablero[coord_x, coord_y] = "-"
            TABLERO_OCULTO[coord_x, coord_y] = "-"
            print("Has fallado!")
            print(tablero)
            
        elif tablero[coord_x, coord_y] == "X":
            print("Disparo previamente realizado!")
            print(tablero)

        elif tablero[coord_x, coord_y] == "-":
            print("Disparo previamente realizado!")
            print(tablero)

def barco_aleatorio(eslora, tablero):
    # Posicionar barcos de manera aleatoria
    np.random.seed(4)
    coord_x_barco = np.random.randint(0, 10)
    coord_y_barco = np.random.randint(0, 10)
    np.random.seed(3)
    orien = np.random.choice(["N", "S", "E", "O"])
    

    if orien == "E":
        print(orien, coord_x_barco, coord_y_barco)
        tablero[coord_x_barco, coord_y_barco: coord_y_barco + eslora] = "O"
        print(tablero)
    
    if orien == "S":
        print(orien, coord_x_barco, coord_y_barco)
        tablero[coord_x_barco: coord_x_barco + eslora, coord_y_barco] = "O"
        print(tablero)
    

TABLERO = init_tablero(fill= " ")
TABLERO_MAQ = init_tablero(fill = " ")
TABLERO_OCULTO = init_tablero(fill= "S", maquina_oc=True)