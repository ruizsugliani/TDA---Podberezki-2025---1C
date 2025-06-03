'''
⭐⭐ Dada una matriz booleana de n x m queremos encontrar la mayor submatriz cuadrada cuyos elementos sean sólo “true”.
Diseñar un algoritmo mediante programación dinámica para resolverlo.

Pensemos que en cada posición de la matriz guardamos el cuadrado de n x n que termina en ella cuyos valores son sólo "true".
Para las posiciones de la primer columna la máxima submatriz cuadrada será 1 para aquellos que tengan el valor "true" y 0 los de caso contrario.
Para las posiciones de la primer fila la máxima submatriz cuadreada será 1 para aquellos que tengan el valor "true" y 0 los de caso contrario.
Para aprovechar el optimo calculado para esas celdas, al iterar las demás "que se encuentran mas adentro de la matriz" debemos ver si:
    - La celda anterior en la misma columna.
    - La celda anterior en la misma columna y en la anterior fila.
    - La celda anterior en la misma fila fila.
Tienen el mismo valor mayor a cero, en tal caso todas cierran una submatriz de tal valor, por lo tanto podemos aprovechar el mismo si la celda actual tiene true.
Por lo tanto sabemos que si esta celda expande la submatriz de dichas posiciones, la misma tendrá:
    Opt[i][j] = Opt de alguna de esas celdas ya que valen todas lo mismo + 2 * sqrt(Opt de alguna de esas celdas ya que valen todas lo mismo) + 1
Por otro lado:
    Opt[i][j] = 0 si M[i][j] = 0
    Opt[i][j] = 1 si sus 3 adyacentes valen distinto.
    
Podemos guardar la posicion de la celda cuya maxima submatriz cuadrada finaliza en ella, ya que el Opt en ella nos dirá de cuánto es esa submatriz.
'''

def submatriz_maxima(M, n):
    Opt = [ [0 for _ in range(n)] for _ in range(n) ]
    max_subm_i, max_subm_j = None, None
    
    for j in range(n):
        if M[0][j] == 1:
            Opt[0][j] = 1
            if max_subm_i == max_subm_j and max_subm_j == None:
                max_subm_i = 0
                max_subm_j = j

    for i in range(n):
        if M[i][0] == 1:
            Opt[i][0] = 1
            if max_subm_i == max_subm_j and max_subm_j == None:
                max_subm_i = i
                max_subm_j = 0
    
    for i in range(1, n):
        for j in range(1, n):
            if M[i][j] == 0:
                Opt[i][j] = 0
            else:
                ady_1 = Opt[i][j-1]
                ady_2 = Opt[i-1][j]
                ady_3 = Opt[i-1][j-1]
                if ady_1 == ady_2 and ady_2 == ady_3 and ady_3 > 0:
                    Opt[i][j] = ady_1 + 2 * ady_1**(1/2) + 1
                    if (max_subm_i == max_subm_j and max_subm_j == None) or (Opt[i][j] > Opt[max_subm_i][max_subm_j]):
                        max_subm_i = i
                        max_subm_j = j

    return Opt, Opt[max_subm_i][max_subm_j]

M = [
    [1,0,1,0,1],
    [0,0,1,1,0],
    [1,1,1,1,0],
    [1,1,1,0,1],
    [1,1,1,0,0]
]

print(submatriz_maxima(M, 5))