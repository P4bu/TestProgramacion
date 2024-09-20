def movimiento_caballo(fila_inicial, columna_inicial):
    # Inicializo el tablero
    tablero = [[0 for _ in range(8)] for _ in range(8)]
    
    # Marco las casillas negras
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                tablero[i][j] = 1

    # Ajustar la posición inicial
    inicial = (fila_inicial - 1, columna_inicial - 1)

    # Listo los posibles movimientos del caballo
    movidas = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) == 3 and (i, j) != (0, 0):
                fila_adyacente = inicial[0] + i
                columna_adyacente = inicial[1] + j
                if 0 <= fila_adyacente < 8 and 0 <= columna_adyacente < 8:
                    movidas.append((fila_adyacente, columna_adyacente))

    # Filtro los movimientos alcanzables
    alcanzables = []
    for movida in movidas:
        fila, columna = movida
        if tablero[fila][columna] == 1: 
            alcanzables.append(movida)

    return alcanzables

# Uso
fila_inicial = 4 
columna_inicial = 4  
movimientos = movimiento_caballo(fila_inicial, columna_inicial)

print("Movimientos alcanzables desde ({} ,{}): {}".format(fila_inicial, columna_inicial, movimientos))
