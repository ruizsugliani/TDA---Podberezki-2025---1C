'''
⭐ Se cuenta con una grafo G=(V,E) con capacidad 1 en cada uno de sus ejes. Existen 2 nodos que tomaremos como “s” fuente y “t” sumidero.
Podemos determinar el flujo máximo F entre s-t. Se pide proponer un algoritmo eficiente que dado un valor “k”, determine la cantidad mínima 
de ejes y cuáles de ellos eliminar para que el nuevo flujo máximo sea F-k. Determinar su complejidad y detallar mediante pseudocódigo y 
una explicación cómo funciona.

Sabemos que si el flujo máximo entre s - t es F y cada arista tiene capacidad 1 que entonces el corte mínimo cuenta con F aristas de capacidad 1.
Por lo tanto si dado un valor "k" queremos que el nuevo flujo sea F - k, entonces debemos quitar k aristas del corte mínimo, ni más ni menos. Podemos
entonces aplicar FF a la red de flujo y obtener los flujos entre aristas, el flujo máximo y la red residual. A partir de la red residual buscaremos los
subconjuntos S y T de V, a partir de ellos las aristas del corte mínimo y posteriormente elegiremos k de ellas.
'''