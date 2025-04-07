'''
⭐ Dado un Grafo dirigido, acíclico G(V, E) con pesos en sus aristas y dos vértices “s” y “t”;
queremos encontrar el camino de mayor peso que exista entre “s” y “t”. Resolver mediante programación dinámica.

La complejidad temporal del algoritmo se compone por:
 - Construir diccionario de entrantes y de óptimos -> 2 * O(V) = O(V)
 - Completar el diccionario de entrantes -> O(V + E)
 - Obtener el orden topologico -> 
 - Calcular los optimos dado el orden topologico del grafo -> O(V + E)
 
La complejidad espacial del algoritmo se compone por:
 - Diccionario de entrantes -> O(V + E)
 - Diccionario de óptimos -> O(V)
 - Lista con el orden topológico -> O(V)
'''

def camino_de_mayor_peso(G, s, t):
    vertices = G.obtener_vertices()
    entrantes = {v: set() for v in vertices}
    opt = {v: None for v in vertices}
    
    for v in vertices:
        for w in G.adyacentes(v):
            entrantes[w].add(v)
    
    orden = obtener_orden_topologico(G, s)
    
    for v in orden:
        if not entrantes[v]:
            opt[v] = 0
        else:
            opt[v] = max(opt[e] + G.obtener_peso(e, v) for e in entrantes[v])
    
    return opt

def obtener_orden_topologico(G):
    pass