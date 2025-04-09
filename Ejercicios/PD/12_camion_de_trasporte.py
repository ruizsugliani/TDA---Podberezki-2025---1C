'''
⭐ Un dueño de un camión de transporte se comprometió a trasladar una carga de una ciudad A a la ciudad B.
Para realizar el recorrido puede optar por diferentes caminos que pasan por diferentes ciudades intermedias.
Nos acerca un mapa donde para cada tramo que une las diferentes ciudades indica el costo de realizar el mismo.
Vemos que algunos costos son positivos (combustible, peaje, etc) y otros negativos o cero (yendo por esos tramos 
puede ganar unos pesos haciendo algunos encargos "particulares"). Nos solicita que le informemos cuál sería el
recorrido óptimo para minimizar el gasto total del viaje. Presentar un algoritmo polinomial utilizando programación 
dinámica que lo resuelva.

Pensemos al mapa como un grafo G tal que las ciudades representen los vértices y los tramos que las unen indican los costos.
Sabemos que desde la ciudad A el costo óptimo para llegar a sí misma es de cero, este es nuestro caso base, para los demás casos
podemos considerar el órden topológico entre ciudades comenzando desde A y que en un principio el costo para llegar a las demás
ciudades es infinito. Una vez obtenido el orden topológico comenzamos a iterar
estas ciudades donde lo que nos importa es considerar el costo que signifique venir de una ciudad anterior más moverse de ella a esta.
Es decir, para toda ciudad I el Opt(I) será igual al menor valor que signifique venir de alguna de las J ciudades anteriores en el orden
más el costo de moverse de J a I y por lo tanto:

Opt(I) = min(Opt[J] + G.obtener_peso(J, I)) con J una ciudad necesariamente anterior a I y por ende existiendo la arista (J, I) en G.
'''
from utils import grafo

def optimizar_traslado(A: str, B :str, G: grafo):
    ciudades = G.obtener_vertices()
    ciudades_anteriores = {c: set(G.obtener_entrantes(c)) for c in ciudades}
    
    opt = {c: float('inf') for c in ciudades_ordenadas}
    ciudades_ordenadas = G.orden_topologico()
    opt[A] = 0
    
    # Construímos los óptimos.
    n = len(ciudades)
    for i in range(1, n):
        for j in range(i):
            if not G.estan_unidos(j, i):
                continue
            Cj = ciudades_ordenadas[j]
            Opt_j = opt[Cj]
            
            if Opt_j + G.obtener_peso(j, i) < opt[i]:
                opt[i] = Opt_j + G.obtener_peso(j, i)
    
    # Reconstruímos la solución.
    res = []
    i = opt[B]
    
    while i != A:
        res.append(i)
        for j in ciudades_anteriores[i]:
            if opt[j] + G.obtener_peso(j, i) == opt[i]:
                i = j
                break
    
    res.reverse()
    return res