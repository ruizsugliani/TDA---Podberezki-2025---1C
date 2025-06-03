'''
Sea "n" la cantidad de filas y columnas.
Sea F el arreglo de largo "n" donde F_i indica la cantidad de celdas a pintar de negro en la fila "i"
Sea C el arreglo de largo "n" donde C_j indica la cantidad de celdas a pintar de negro en la columna "j"
Sea T el tablero de tamaño "n x n" inicialmente con las celdas todas en blanco (valor 0)
Sea Coloraciones el arreglo de tableros que cumplan las coloraciones pedidas
Sean i = j = 1 inicialmente (tomamos como indice inicial al 1)
Sean PintadasEnF y PintadasEnC arreglos de tamaño "n" inicialmente con 0 en cada posición.

ObtenerColoraciones(F, C, n):
    Coloraciones = []
    T = ArmarTablero(n)
    i = j = 1
    PintadasEnF = PintadasEnC = Lista de tamaño "n" con ceros en sus posiciones
    Colorear(T, F, C, Coloraciones i, j, n, PintadasEnF, PintadasEnC)
    retornar Coloraciones

ArmarTablero(n)
    Para i = 1 hasta n
        Para j = 1 hasta n
            T[i, j] = 0
    Retornar T

ObtenerProximaCelda(i, j, n)
    Si j == n:
        i = i + 1
        j = 1

    Sino
        i = i
        j = j + 1
    
    Retornar i, j

Función EsPosiblePintarEstaCelda(F, C, PintadasEnF, PintadasEnC, i, j, n):
    Si PintadasEnF[i] < F[i] y PintadasEnC[j] < C[j]:
        celdas_restantes_fila = n - j
        celdas_restantes_columna = n - i
        Si PintadasEnF[i] + celdas_restantes_fila >= F[i] y PintadasEnC[j] + celdas_restantes_columna >= C[j]:
            Retornar Verdadero
    Retornar Falso
    
EsColoracionValida(F, C, PintadasEnF, PintadasEnC)
    Para i = 1 hasta N
        Si F[i] != PintadasEnF[i] o C[i] != PintadasEnC[i]
            Retornar Falso
    Retornar Verdadero

Colorear(T, F, C, Coloraciones, i, j, n, PintadasEnF, PintadasEnC)
    Si i > n y EsColoracionValida(F, C, PintadasEnF, PintadasEnC)
        Agrego en Coloraciones una copia de T
        Retornar
    
    prox_i, prox_j = ObtenerProximaCelda(i, j, n)
    
    Si EsPosiblePintarEstaCelda(F, C, PintadasEnF, PintadasEnC, i, j, n)
        T[i, j] = 1
        PintadasEnF[i] += 1
        PintadasEnC[j] += 1
        
        Colorear(T, F, C, Coloraciones, prox_i, prox_j, n, PintadasEnF, PintadasEnC)
        
        T[i, j] = 0
        PintadasEnF[i] -= 1
        PintadasEnC[j] -= 1
    
    Colorear(T, F, C, Coloraciones, prox_i, prox_j, n, PintadasEnF, PintadasEnC)
'''