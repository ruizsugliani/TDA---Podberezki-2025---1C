'''
Se cuenta con un vector V de “n” elementos. Este vector visto de forma circular está ordenado.
Pero no necesariamente en la posición inicial se encuentra el elemento más pequeño.
Deseamos conocer la cantidad total de rotaciones que presenta “V”.
Ejemplo: V = [6, 7, 9, 2, 4, 5] se encuentra rotado en 3 posiciones. 
Podemos hacerlo en tiempo O(n) por fuerza bruta. Presentar una solución utilizando división y conquista que mejore esta complejidad.

Dado que debemos mejorar una complejidad lineal, vamos a buscar una complejidad logarítmica. La idea es encontrar el primer elemento
de menor valor ya que sabemos de antemano que el arreglo se encuentra ordenado si lo vemos de forma circular. Nos interesa encontrar
dicho numero dado que todos los anteriores deberían encontrarse luego del ultimo para estar ordenado "sin verlo" de forma circular.
Vamos a tomar el elemento del medio del arreglo (M) y compararlo con el primero(I), si V[M] < V[I] entonces sabemos que entre las posiciones
[I:M] del arreglo se encuentra el numero que buscamos, en caso contrario significa que [I:M] está ordenado y debemos contemplar la segunda mitad
del arreglo. Tenemos entonces A = 1 llamado recursivo por nivel y B = 2 mitades en las cuales dividimos el arreglo por cada nivel de recursión, finalmente
f(n) = O(1) dado que solo realizamos una comparación, por lo tanto la complejidad temporal es O(n log n) y la complejidad espacial O(1).
'''
def cant_rotaciones(V):
    return _cant_rotaciones(V, 0, len(V) - 1)

def _cant_rotaciones(V, ini, fin):
    if fin - ini == 1:
        if V[fin] < V[ini]:
            return fin
        return ini
    
    m = (ini + fin) // 2
    
    if V[m] < V[ini]:
        return _cant_rotaciones(V, ini, m)
    return _cant_rotaciones(V, m, fin)

def rotaciones(V):
    ix_res = _obtener_menor_ix(V, 0, len(V)-1)
    return ix_res

def _obtener_menor_ix(V, ini, fin):
    if fin - ini == 1:
        return ini if V[ini] < V[fin] else fin
    m = (ini + fin) // 2
    if V[m] > V[fin]:
        return _obtener_menor_ix(V, m, fin)
    return _obtener_menor_ix(V, ini, m)

print(rotaciones([9,2,4,5,6,7]))
print(rotaciones([7,9,2,4,5,6]))
print(rotaciones([6,7,9,2,4,5]))
print(rotaciones([5,6,7,9,2,4]))
print(rotaciones([4,5,6,7,9,2]))
print(rotaciones([2,3,4,5,6,7]))