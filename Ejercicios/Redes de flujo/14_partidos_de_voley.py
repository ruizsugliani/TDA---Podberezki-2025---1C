'''
⭐ Un grupo de "n" amigos participan en un torneo de voley. En cada partido se debe presentar una planilla de "y" jugadores.
Se juegan partidos 1 vez por semana, durante un periodo de 9 meses. Para lograr que juegue la mayoría se propuso que cada amigo 
no juegue más de 4 partidos. Esos partidos deben estar lo más separados posible, por lo que no pueden jugar más de 1 partido por mes.
Finalmente se tiene que tener en cuenta que algunos amigos en ciertas fechas no pueden asistir por cuestiones personales. Proponer un
algoritmo polinomial que utilizando esta información realice la asignación de jugadores por partido 
(o que indique que con esas restricciones no es posible realizarlo).

Generaremos un grafo para modelar este problema y posteriormente aplicaremos FF, si el flujo obtenido equivale a "y" * "cant_partidos" significa
que para cada uno de los partidos hemos encontrado una asignación de los jugadores necesarios por planilla. Para modelar las restricciones y que el grafo
sea una red de flujo debemos:
    - Crear el nodo S.
    - Crear el nodo T.
    - Creamos N nodos, uno por cada jugador y unimos S a cada uno de ellos con una arista de capacidad 4 en representación de la cantidad máxima de veces que cada uno puede jugar.
    - Por cada jugador crearemos 9 nodos que representen los meses, algo asi como mes_i_n donde i es el mes (1 <= i <= 9) y en el jugador, el nodo del jugador tendrá una arista hacia
    cada uno de estos nodos de capacidad 1 en representación de la cantidad de partidos que puede jugar por mes.
    - Crearemos P nodos, uno por cada partido donde uniremos cada nodo mes_i_n con cada partido que se encuentre en tal mes con capacidad 1 representando la cantidad de veces que el
    jugador n puede jugar ese partido (en caso de que dicha fecha el mismo pueda ir al partido).
    - Finalmente desde cada nodo P habrá una arista hacia T de capacidad "y" que representa la cantidad de jugadores que necesita para esa planilla.
    
Construcción de la red:
    - O(N + 9 * N + 9 * N * P + P) = O(N * P) debido a la construcción tanto de los nodos como las aristas que los unen.

Ford-Fulkerson:
    - O(V * E^2) donde en nuestro algoritmo |V| = 9 * N * P = N * P y donde |E| = N + 9 * N * P + P y por lo tanto
    tenemos que es O( (N * P) + (N * P)^2 ).
    
Reconstrucción de la solución:
    - Por cada jugador debemos ver los meses y en que partidos juega, esto significa observar si el flujo de la arista mes_i_n -> partido_p = 1 y por lo
    tanto la complejidad es O(9 * N * P) = O(N * P)
'''