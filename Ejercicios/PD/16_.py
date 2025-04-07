'''
⭐ Se conoce como “Longest increasing subsequences” al problema de, dado un vector de numérico,
encontrar la subsecuencia más larga de números (no necesariamente consecutivos) donde cada elemento 
sea mayor a los anteriores. Ejemplo: En la lista →  2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7.
Podemos ver que la subsecuencia más larga es de longitud 6 y corresponde a la siguiente “1, 2, 3, 4, 6, 7”.
Resolver el problema mediante programación dinámica.

Tendremos una lista con óptimos donde guardaremos los resultados de la subsecuencia incremental mas larga encontrada
hasta el índice I. Para ello tendremos el caso base del primer número de la lista, donde hasta I = 1 el Opt[I] = 1.
Posteriormente comenzaremos a iterar desde 1..N con N la cantidad de elementos en la lista pasada por parámetro, en cada
caso evaluaremos si el elemento anterior es menor al actual, en tal caso contabilizamos Opt[I] = Opt[I-1] + 1, en caso contrario
solo contabilizaremos O(I-1), iremos guardando I al encontrar un numero menor a este para al momento de la reconstrucción hacer uso del mismo.
Al momento de la reconstrucción comenzaremos desde el último I guardado y lo insertaremos en una lista a devolver si el I-1 es efectivamente menor
en la lista original, sino lo ignoramos.
'''

def longest_increasing_subsequences(V):
    n = len(V)
    opt = [None for _ in range(n)]
    
    opt[0] = 1
    ultimo = 0
    for i in range(1, n):
        if V[i-1] < V[i]:
            opt[i] = opt[i-1] + 1
            ultimo = i
        else:
            opt[i] = opt[i-1]
    
    res = []
    i = ultimo
    while i > 0:
        if opt[i] > opt[i-1]:
           res.append(V[i])
        i -= 1
    
    if V[0] < V[1]:
        res.append(V[0])
    
    res.reverse()
    return res, opt

print(longest_increasing_subsequences([2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]))
print(longest_increasing_subsequences([10,9,2,5,3,7,101,18]))
print(longest_increasing_subsequences([0,1,0,3,2,3]))
print(longest_increasing_subsequences([7,7,7,7,7,7,7]))
# [2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]
# [1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6]