'''
Dado un grafo G queremos hallar el IS de mayor tamaño posible.

Sea Parcial una lista cuyo primer elemento es un entero inicializado en cero y cuyo segundo elemento es una lista vacía.
Sea Optimo una lista igual que Parcial inicialmente.

Buscaremos agregar vértices a parcial de modo que cuando parcial conforme un IS lo compararemos a Optimo y si tiene más elementos entonces será el nuevo optimo.

Debemos probar agregar o no un vértice con lo cual tenemos O(2^n) posibles estados más el trabajo en cada uno de estos estados, el mismo depende de la complejidad de
puedoAgregarlo donde me fijo que cada vertice de parcial no sea adyacente al vértice que quiero agregar en O(n). Finalmente la complejidad será O(2^n * n). Otra poda
además de las realizadas por puedoAgregarlo es calculando la cantidad de vertices en la solución parcial más los que no exploré, si esta cantidad es menor o igual al
óptimo entonces no lo podré mejorar.

MaxIndependentSet(G):
    Parcial = [0, []]
    Optimo = [0, []]
    vertices = G.obtener_vertices()
    i = 0
    
    Optimo = _MaxIndependentSet(G, Parcial, Optimo, vertices, i)
    
    returno Optimo
    
_MaxIndependentSet(G, Parcial, Optimo, vertices, i):
    if i >= len(vertices):
        return Optimo

    if Parcial[0] + (len(vertices) - i) <= Optimo[0]:
        return Optimo

    if puedoAgregarlo(G, Parcial, vertices[i]):
        Parcial[0] += 1
        Parcial[1].append(vertices[i])
        
        Optimo = _MaxIndependentSet(G, Parcial, Optimo, vertices, i+1)
        
        Parcial[0] -= 1
        Parcial[1].pop()  
    
    Optimo = _MaxIndependentSet(G, Parcial, Optimo, vertices, i+1)
    return Optimo
'''