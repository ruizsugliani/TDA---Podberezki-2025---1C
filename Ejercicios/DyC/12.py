'''
Dado “L” un listado ordenado de “n” elementos y un elemento “e” determinado.
Deseamos conocer la cantidad total de veces que “e” se encuentra en “L”.
Podemos hacerlo en tiempo O(n) por fuerza bruta.
Presentar una solución utilizando división y conquista que mejore esta complejidad.

Debido a que el listado viene ordenado, las apariciones de "e" son entonces consecutivas.
Aplicaremos un enfoque similar a búsqueda binaria, tenemos los siguientes casos:
    - Si el elemento del medio de mi arreglo actual es mayor a "e" entonces puedo descartar la segunda mitad del arreglo actual.
    - Si el elemento del medio de mi arreglo actual es menor a "e" entonces puedo descartar la primera mitad del arreglo actual.
    - Si el elemento del medio de mi arreglo actual es igual a "e" entonces debo seguir contemplando ambas mitades.
'''

def apariciones(L, e):
    return _apariciones(L, e, 0, len(L) - 1)

def _apariciones(L, e, ini, fin):
    if fin <= ini:
        return 1 if L[ini] == e else 0
    
    m = (ini + fin) // 2
    if L[m] < e:
        return _apariciones(L, e, m + 1, fin)
    if L[m] > e:
        return _apariciones(L, e, ini, m - 1)
    return _apariciones(L, e, ini, m) + _apariciones(L, e, m + 1, fin)

assert(apariciones([1, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6], 1) == 1)
assert(apariciones([1, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6], 2) == 5)
assert(apariciones([1, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6], 5) == 2)
assert(apariciones([1, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6], 6) == 3)

print({"0": 1} + {"0": 2})