'''
⭐ En un grafo se conoce como conjunto independiente a un subconjunto de vértices del mismo tal que ninguno sea adyacente a otro.
Es decir, es un conjunto X de vértices tal que para ningún par de ellos existe alguna arista que los conecte. No se conoce un algoritmo
eficiente que resuelva el problema. Sin embargo, para algunos casos especiales de grafos si es posible. Considerar el siguiente caso: 
Un grafo es un camino si se pueden escribir sus nodos como una sucesión V1, V2, ..., Vn donde cada nodo Vi tiene un eje únicamente con Vi-1 y Vi+1.
(Excepto en los extremos donde solo tienen un eje con el siguiente o el anterior). Considerar que cada nodo tiene un peso entero positivo. Construir
un algoritmo utilizando programación dinámica que encuentre el set independiente de mayor peso.

Pensemos en nuestro caso base de V1, para el mismo, hasta V1 el set independiente de mayor peso se constituye solo por V1, por lo tanto Opt[V1] = V1.
Ahora pensemos en el caso general, si Vi pertenece al set independiente entonces Vi-1 no puede pertenecer al igual que Vi+1 por tratarse de un grafo
no dirigido. Entonces dados j, i con j = i - 1 podemos pensar en que Opt[i] = max(Opt[j], Opt[j - 1] + Vi) y dicho esto agregamos otro caso base para V2
donde su óptimo equivale a Opt[V2] = max(V1, V2).

Finalmente la complejidad temporal es O(N) con N la cantidad de vertices del camino ya que creamos un arreglo de óptimos en O(N), luego recorremos las
N posiciones calculando el óptimo con una comparación y accesos en O(1) y finalmente volvemos a recorrer el arreglo de adelante hacia atrás para reconstruir
la solución también en O(N). Por el lado de la complejidad espacial, la complejidad también es O(N) por el arreglo de los N óptimos.
'''

def max_set_independiente_en_camino(camino):
    n = len(camino)
    opt = [0 for _ in range(n)]
    opt[0] = camino[0]
    opt[1] = max(opt[0], camino[1])
    
    for i in range(2, n):
        opt[i] = max(opt[i-1], opt[i-2] + camino[i])
    
    i = n -1
    res = []
    while i >= 0:
        # Casos base
        if i == 0 or i == 1:
            res.append(camino[i])
            break

        # Caso general
        if opt[i] == opt[i-2] + camino[i]:
            res.append(camino[i])
            i -= 2
        else:
            i -= 1
    
    res.reverse()
    return res

print(max_set_independiente_en_camino([1, 2, 3, 4, 5]))
print(max_set_independiente_en_camino([17, 3, 42, 8]))
print(max_set_independiente_en_camino([1, 5, 1]))
print(max_set_independiente_en_camino([1, 5, 8]))