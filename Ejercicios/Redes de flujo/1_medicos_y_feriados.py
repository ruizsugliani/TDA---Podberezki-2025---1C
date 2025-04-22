'''
⭐La sala de guardia de un hospital tiene que tener al menos un médico en todos los feriados y en los fines de semana largos de feriados.
Cada profesional indica sus posibilidades: por ejemplo alguien puede estar de guardia en cualquier momento del fin de semana largo del 9 de julio
(p. ej. disponibilidad de A para el 9 de julio = (Jueves 9/7, Viernes 10/7, Sábado 11/7, Domingo 12/7)), también puede suceder que alguien pueda 
sólo en parte (por ejemplo, disponibilidad de B para 9 de julio = (Jueves 9/7, Sábado 11/7, Domingo 12/7)). Aunque los profesionales tengan múltiples 
posibilidades, a cada uno se lo puede convocar para un solo día (se puede disponer de B sólo en uno de los tres días que indicó). Para ayudar a la
sala de guardia a planificar cómo se cubren los feriados durante todo el año debemos resolver el problema de las guardias: Existen k períodos de
feriados (por ejemplo, 9 de julio es un período de jueves 9/7 a domingo 12/7, en 2019 Día del Trabajador fue un período de 1 día: miércoles 1 de mayo, etc.).
Dj es el conjunto de fechas que se incluyen en el período de feriado j-ésimo. Todos los días feriados son los que resultan de la unión de todos los Dj.
Hay n médicos y cada médico i tiene asociado un conjunto Si de días feriados en los que puede trabajar (por ejemplo B tiene asociado los días Jueves 9/7,
Sábado 11/7, Domingo 12/7, entre otros). Proponer un algoritmo polinomial (usando flujo en redes) que toma esta información y devuelve qué profesional 
se asigna a cada día feriado (o informa que no es posible resolver el problema) sujeto a las restricciones:
    - Ningún profesional trabajará más de F días feriados (F es un dato), y sólo en días en los que haya informado su disponibilidad.
    - A ningún profesional se le asignará más de un feriado dentro de cada período Dj.

Para construir la red de flujo, además de los nodos S y T debemos:
    - Crear los N nodos de los médicos, donde desde S va un eje hacia cada uno de ellos con capacidad F por la cantidad máxima de días feriado que puede trabajar un médico.
    - Como ningun medico puede trabajar mas de un feriado de un mismo período D, existirán D períodos por cada médico, por ende existirán D * N nodos de este tipo de la forma periodo_D_N
    con una arista desde el nodo del médico hasta este nodo de capacidad 1 representando que solo puede trabajar un día de dicho período.
    - Por cada uno de estos períodos, habrá una arista hacia un nodo d que represente uno de los días de ese período de feriados en caso de que dicho médico pueda trabajar dicho feriado
    y de capacidad 1 representando si trabaja o no tal día.
    - Finalmente desde los nodos de los días hacia el nodo T existirá un eje de capacidad 1 dado que con un medico que trabaje dicho día nos alcanza.

Complejidad del armado de la red:
    - O(n + n * k * d) = O(n * k * d)

Complejidad de FF:
    - O(V * E^2) donde |V| = n + n * k * d = n * k * d y |E| = 

Complejidad del armado de asignaciones:
    - Basta con mirar por cada medico y período si alguno de esos días tiene flujo igual a 1, es decir si f(periodo_D_N, d) = 1 y por lo tanto la complejidad es O(N * D * d).
'''