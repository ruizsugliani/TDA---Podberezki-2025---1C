'''
⭐⭐ Se define el problema 2-Partition de la siguiente manera: Se cuenta con un conjunto de “n” elementos. Cada uno de ellos tiene un valor asociado.
Se desea separar los elementos en 2 conjuntos que cumplan con: La suma de los valores de cada conjunto sea igual entre ellos. No se conoce un algoritmo 
eficiente para resolver este problema. Sin embargo - al igual que otros problemas puede ser resuelto utilizando programación dinámica de forma pseudopolinomial.
Presente una solución al problema utilizando dicha metodología.

Trataremos el problema 2-Partition como un caso especial del problema de la mochila, en este caso el K del problema de la mochila equivale a la suma de los elementos
del conjunto dividido dos. Luego el conjunto de elementos del tipo (peso, valor) del problema de la mochila en 2-Partition son los elementos del conjunto que son números
y por ende serían elementos del tipo (valor_del_elemento, valor_del_elemento). Finalmente el problema se resuelve de la misma manera, teniendo entonces la ecuación
de recurrencia: Opt[i][j] = max(Opt[i][j-v] + v, Opt[i-1][j]) para el caso donde considero incluir al elemento actual en el subconjunto A (ya que A + B = C el conjunto original)
y con "i" el elemento iterado actualmente, "j" el "peso soportado de la mochila" en la iteración actual.
'''

def _2_partition(S):
    total = sum(S)
    if total % 2 != 0:
        return None  # No se puede partir en dos sumas iguales
    
    K = total // 2
    n = len(S)
    
    opt = [[0 for _ in range(K+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, K+1):
            v = S[i-1]
            if j >= v:
                opt[i][j] = max(opt[i][j-v] + v, opt[i-1][j])
            else:
                opt[i][j] = opt[i-1][j]
    
    A = []
    i, j = n, K
    while i > 0 and j > 0:
        v = S[i-1]
        if j >= v and opt[i][j] == opt[i][j - v] + v:
            A.append(v)
            j -= v
        i -= 1

    # Ahora construimos B como lo que quedó fuera de A
    # Para eso usamos una copia temporal de S
    S_copy = S[:]
    for v in A:
        S_copy.remove(v)
    
    B = S_copy
    A.reverse()
    return A, B, S


print(_2_partition([3, 1, 1, 2, 2, 1]))
print(_2_partition([4, 5, 6, 7, 8]))
print(_2_partition([
    3, 1, 4, 2, 2, 1, 7, 5, 6, 8, 9, 10, 11, 3, 2, 4,
    6, 5, 1, 3, 2, 8, 9, 7, 1, 2, 4, 6
]))