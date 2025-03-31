'''
Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” 
números naturales ordenados en forma creciente (m >= n). En el vector no hay números repetidos.
Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]. Solución: 6. 
Proponer un algoritmo de tipo división y conquista que resuelva el problema en tiempo inferior a lineal.
Expresar su relación de recurrencia y calcular su complejidad temporal.

Sea la lista L de naturales.
Sea L_1 la primera mitad de la lista y L_2 la segunda.
'''

def menor_no_incluido(arr):
    return _menor_no_incluido(arr, 0, len(arr) - 1)

def _menor_no_incluido(arr, ini, fin):
    if fin <= ini:
        return None
    
    c = (ini + fin) // 2
    res_izq = _menor_no_incluido(arr, ini, c)
    res_der = _menor_no_incluido(arr, c+1, fin)
    
    if res_izq is not None:
        return res_izq
    
    if arr[c+1] - arr[c] > 1:
        return arr[c] + 1
    
    return res_der

assert(menor_no_incluido([1, 3, 4, 5, 6]) == 2)
assert(menor_no_incluido([1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]) == 6)
assert(menor_no_incluido([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 22]) == 15)