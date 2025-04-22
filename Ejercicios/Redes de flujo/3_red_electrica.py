'''
⭐ La compañía eléctrica de un país nos contrata para que le ayudemos a ver si su red de transporte desde su nueva generadora hidroeléctrica 
hasta su ciudad capital es robusta. Nos otorgan un plano con la red eléctrica completa: todas las subestaciones de distribución y red de cableados de alta tensión.
Lo que quieren que le digamos es:
¿Cuantas secciones de su red se pueden interrumpir antes que la ciudad capital deje de recibir la producción de la generadora?
¿Puede informar cual es el subconjunto de ejes cuya falla provoca este problema?
(Sugerencia: investigue sobre el Teorema de Menger)

El teorema de Menger dice:
(Menger, 1927) Sean u y v dos vértices no adyacentes en un grafo (no dirigido) conexo G = (V ; E). Entonces el máximo número de 
caminos disjuntos en vértices de u a v es igual al mínimo numero de vertices que hay que sacar para desconectar u de v.

Según Wikipedia:
el Teorema de Menger dice que en un gráfico finito, el tamaño de un conjunto de corte mínimo es igual al número máximo de caminos disjuntos que se pueden encontrar entre
cualquier par de vértices.

Contamos con la red de flujo como dato, sabemos que la nueva generadora hidroeléctrica es el nodo S, y que la ciudad capital es el nodo T. También contamos con todas
subestaciones de distribución (nodos conmutadores) y la red de cableados de alta tensión (ejes entre los nodos de la red). Observando la definicion del teorema de Menger
si las capacidades de los ejes son todas 1 y tras aplicar FF obtenemos el corte mínimo, entonces observando las aristas que forman parte del mismo, si quitamos por cada una
de esas aristas uno de los vértices (nodos conmutadores) entonces desconectamos S y T provocando entonces que deje de llegar flujo desde S a T. Respondiendo a la primera pregunta
entonces la cantidad de aristas que forman parte del corte mínimo menos 1 son la cantidad de "secciones a interrumpir" antes que la ciudad capital deje de recibir energía.
Y por lo tanto el subconjunto de ejes cuya falla provoca este problema es el subconjunto de ejes del corte minimo.
'''