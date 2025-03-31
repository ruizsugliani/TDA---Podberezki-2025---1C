'''
07
------------------------------------------------------------------------------------------------------------------------------------
Contamos con:
    - N socios.
    - lista de pares de socios que se conocen.
Modelaremos un grafo donde cada vértice Vi representará a uno de los N socios y mediante la lista de pares de socios conocidos iremos trazando
las aristas que los unen, es decir, si el socio 1 y 2 se conocen en la lista estará el par (1, 2) y por lo tanto en el grafo que modelaremos habrá
una arista que una V1 y V2 (claramente G es no dirigido y tampoco es pesado). Posteriormente comenzaremos a iterar los vértices del grafo, si el vértice
actual tiene un grado menor a 4 entonces lo eliminamos de G ya que significa que no conoce a 4 invitados, al encontrar un caso de un vértice que debemos quitar
de G tenemos que volver a revisar el grafo nuevamente porque puede suceder que un vértice anteriormente iterado conocía a 4 socios y este era uno de ellos (haremos
uso de una variable booleana para saber si tenemos que volver a revisar los vértices, la misma antes de la iteración de V tendrá valor false y en caso de encontrar uno
que debamos quitar se cambiara el mismo a true). Una vez iterados todos los vértices si la variable booleana sigue en false significa que no se quitaron más vértices y
por ende en G quedaron todos los vértices que representan los socios a invitar, en caso contrario volvemos a iterar V. Finalmente devolvemos los vértices de G.

Dado que N = |V(G)| y M = |E(G)| para construir G tenemos que la complejidad es O(V + E) y a lo sumo eliminamos todos los vértices con lo cual la complejidad queda como
O(V* (V + E))
'''