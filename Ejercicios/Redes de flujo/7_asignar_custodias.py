'''
⭐ La policía de la ciudad tiene “n” comisarías dispersas por la ciudad. Para un evento deportivo internacional deben asignar
la custodia de “m” centros de actividades. Una comisaría y un centro de actividades pueden ser emparejados si y sólo si la
distancia entre ellos no es mayor a un valor "d". Contamos con la distancia entre todos los centros y las comisarías. Una comisaría
sólo puede custodiar un centro. El centro puede ser custodiado por una comisaría. Determinar si es posible la asignación de tal forma 
que todos los centros estén custodiados.

¿Cómo modificaría la resolución del problema si en lugar de que cada centro de actividades i tenga que ser asignado a una sola comisaría,
tenga que ser asignado a m_i comisarías? ¿Cómo modificaría la resolución del problema si además hubiera una restricción entre comisarías 
que implicaría que una comisaría Ni y una Nj no pudieran ser asignadas juntas a un centro Mi?
¿Para qué casos dejaría de ser eficiente la resolución?

Vamos a construir un grafo G = (V, E) sobre el cual aplicaremos Ford-Fulkerson, de modo que si el flujo obtenido es igual a la cantidad de centros de
actividades (osea igual a M) es que encontramos una solución donde cada uno de esos M centros es custodiado por una de las N comisarias.
Dado que cada comisaría solo puede custodiar un centro haremos lo siguiente:
    - El grafo G posee como vértices al conjunto resultante de {S, T} + {N_comisarias} + {M_centros} donde S y T son la fuente y el sumidero respectivamente.
    - Existirá una arista de peso 1 dirigida desde S a cada uno de las N comisarías.
    - Existirá una arista de peso 1 dirigida desde cada uno de los M centros hacia T.
    - Existirá una arista de peso 1 dirigida por cada par (Ni, Mj) de comisarías y centros a una distancia <= "d".
Por lo tanto encontrar un camino entre una comisaría y un centro representan haber encontrado una asignación válida para la custodia, además de que tanto la
comisaría como el centro no serán parte de otro par de comisaria-centro seleccionado en el resultado final.

Tenemos entonces que la complejidad temporal se compone del armado del grafo (1), la aplicación de Ford-Fulkerson (2) y la búsqueda de las custodias asignadas (3), esto es:
    1) O(N * M) con N la cantidad de comisarias y M la cantidad de centros.
    2) O(E * M) con E la cantidad de aristas y M la cantidad de centros dado que en caso de haber solución, se encontraron M caminos.
    3) O(N * M) por tener que buscar para cada comisaría si se asignó o no a algún centro.
Finalmente la complejidad es O(N * M) + O(E * M) y en el peor caso cada comisaría se asigna a cada centro, por lo tanto la complejidad temporal final es O(N * M * M) = O(N * M^2).
'''
from utils import grafo as Grafo

def comisarias_y_centros(N, M, d, distancias):
    G = armado_red_flujo(N, M, d, distancias)
    flujos, flujo_max, Gr = G.ford_fulkerson()
    
    if flujo_max != len(M): # No se pudieron asignar M custodias (osea una a cada centro).
        return False

    custodias = []
    for n in N:
        for m in M:
            if flujos[n, m] == 1: # Esta comisaria fue asignada a este centro.
                custodias.append((n, m))
                break
    
    return custodias


def armado_red_flujo(N, M, d, distancias):
    G = Grafo(dirigido=True)
    G.agregar_vertice("S")
    G.agregar_vertice("T")
    
    for n in N: # O(N)
        G.agregar_vertice(n)
        G.agregar_arista("S", n, 1)
    
    for m in M: # O(M)
        G.agregar_vertice(m)
        G.agregar_arista(m, "T", 1)
    
    for n in N: # O(N * M)
        for m in M:
            if distancias.get((n, m), float('inf')) < d:
                G.agregar_arista(n, m, 1)
    
    return G