'''
Dado un vector A de “n” números enteros (tanto positivos como negativos) queremos obtener el subvector 
cuya suma de elementos sea mayor a la suma de cualquier otro subvector en A.  
Ejemplo: Array: [-2, -5, 6, -2, -3, 1, 5, -6]. Solución: [6, -2, -3, 1, 5].
Resolver el problema de subarreglo de suma máxima por división y conquista.

En cada nivel de recursión estaremos realizando un llamado para cada mitad del arreglo actual, por lo tanto tenemos que
usando el teorema del maestro A = 2 y B = 2. Siendo el caso base cuando el arreglo actual tiene un elemento, lo devolvemos.
Al momento de juntar las soluciones estaremos contemplando el resultado del llamado para ambas mitades y además el arreglo que
interseca ambas con el mayor valor. Finalmente tenemos que la complejidad de esto es O(n) puesto que recorremos cada arreglo para
conocer su valor total ademas de recorrer ambos comenzando desde el medio (elemento final del arreglo izquierdo y elemento inicial
del arreglo derecho). Siendo entonces también O(n) la complejidad espacial en caso de ser el resultado todo el arreglo completo.
'''

def maxsubarray(arr):
    return _maxsubarray(arr, 0, len(arr) - 1)

def _maxsubarray(arr, ini, fin):
    if fin <= ini:
        return [arr[ini]]
    
    m = (ini + fin) // 2
    
    izq = _maxsubarray(arr, ini, m)
    der = _maxsubarray(arr, m + 1, fin)
    
    return obtener_maximo_sub_arr(arr, izq, der)

def obtener_maximo_sub_arr(arr, izq, der):
    arr_cruz = []
    arr_cruz.append(izq[-1])
    arr_cruz.append(der[0])
    sum_cruz = izq[-1] + der[0]
    
    max_i = i = len(izq) - 1
    max_j = j = 0
    
    
    
    
