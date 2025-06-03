'''
Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor xi. Todos los xi son valores diferentes. 
Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta (es decir, los hijos 
que tenga y su padre, si tiene). Implementar un algoritmo por división y conquista que obtenga algún mínimo local del árbol en O(logn). 
Justificar apropiadamente la complejidad del algoritmo implementado. Considerar que el árbol tiene en su estructura el nombre del nodo, 
su valor, y las referencias a sus hijos izquierdo y derecho.

Como caso base tendremos que el nodo raiz sea un minimo local donde ya podremos devolver su valor si es menor al de sus hijos, en caso contrario
comenzaremos a buscar hacia la izquierda, es decir haremos uso de una función recursiva que llamaremos para cada nodo que vayamos a analizar, la misma
tendrá como parámetros al nodo actual y el valor del nodo padre. Si el nodo actual es minimo local entonces devolvemos su valor, sino llamamos para el hijo izquierdo
como nodo actual y el valor del nodo actual será el valor del padre en tal llamado, si no encontramos el minimo local en el llamado recursivo al hijo izquierdo entonces
repetimos para el hijo derecho. Tendremos como caso base que el nodo actual no tenga hijos (sea null) por lo tanto para el mismo devolveremos null lo cual representa que 
el llamado hacia este nodo no encontró el minimo local.

Respecto al teorema maestro tenemos A = 2, B = 2, f(n) = O(1)

Si vamos al segundo caso del teorema tenemos que:

f(n) = O(log_B (A))
O(1) = O(log_2 (2))
O(1) = O(1)

Por lo tanto:
T(n) = O(n ^ log_B (A) * log n)
T(n) = O(n ^ 1 * log n)
T(n) = O(n * log n)
'''

def obtener_minimo_local(raiz):
    return _obtener_minimo_local(raiz, float("inf"))

def _obtener_minimo_local(nodo, valor_padre):
    if nodo == None:
        return None
    
    if es_minimo_local(nodo, valor_padre):
        return nodo.valor
    
    minimo_local_izq = _obtener_minimo_local(nodo.hijo_izq, nodo.valor)
    if minimo_local_izq:
        return minimo_local_izq
    return _obtener_minimo_local(nodo.hijo_der, nodo.valor)

def es_minimo_local(nodo, valor_padre):
    valor_hijo_izq = nodo.hijo_izq.valor if nodo.hijo_izq is not None else float("inf")
    valor_hijo_der = nodo.hijo_der.valor if nodo.hijo_der is not None else float("inf")
    return nodo.valor < valor_hijo_izq and nodo.valor < valor_hijo_der and nodo.valor < valor_padre

'''
El explorador Roberto se embarcó en una misión para encontrar el legendario Templo de los Vientos. En el vasto desierto, hay oasis donde puede recoger provisiones 
esenciales como agua y comida. Cada oasis tiene recursos limitados. Sin suficientes provisiones, Roberto no podrá cruzar el desierto. Sólo vamos a considerar el hecho
de tener k cantidad de provisiones (no si son una cosa u otra). Implementar un algoritmo greedy que permita a Roberto llegar al templo con la menor cantidad de paradas
posibles en los oasis. Indicar y justificar la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace,
justificar, si no dar un contraejemplo.

Datos que se reciben:
- Una lista de n elementos que nos indica cuántas provisiones (en cantidad) se pueden conseguir en cada uno de los n oasis. 
- Una lista con las distancias del inicio de la travesía al primer oasis, del primero al segundo, del segundo al tercero, y así hasta el final de la travesía 
(la lista tiene n + 2 elementos).
- La cantidad de provisiones iniciales de Roberto.
- Una constante KM_PROVISION que indica cuántas provisiones se debe consumir para caminar un KM.

- Sea OasisProv una lista de largo N con info en cada posición sobre el oasis en tal posicion.
- Sea Distancias una lista de largo N + 2 donde cada Di representa la distancia entre la posición i y el oasis i + 1.
- Sea K la cantidad de provisiones inicial.
- Sea KM_PROVISION las provisiones que se consumen por cada kilometro.

Pensemos en que dada la posicion actual i queremos llegar al oasis más lejano posible, por lo tanto entre la posición actual y la del siguiente oasis tendremos que consumir
KM_PROVISION * Distancias[i] lo cual si es menor a las K provisiones que tenemos guardamos como OasisMasLejanoPosible, y asi seguimos calculando hasta que no alcancemos dadas las K
provisiones llegar a un oasis, por lo tanto el próximo oasis donde nos pararemos a recoger provisiones será OasisMasLejanoPosible donde K se decrementará en función de los kilometros
recorridos hacia tal oasis y posteriormente le sumaremos las provisiones de ese oasis.
'''

def mision(K, oasis, distancias, KM_PROVISION):
    res = []
    K_act = K
    consumo_hasta_i = 0
    ult_parada = None
    
    for i in range(len(distancias)):
        consumo_hasta_i += KM_PROVISION * distancias[i]
        if consumo_hasta_i < K_act:
            ult_parada = i
        else:
            K_act -= consumo_hasta_i
            K_act += oasis[i]
            
'''
Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar la máxima cantidad de charlas a dar
de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas (devolviendo las charlas que logran esto). Resolver el problema de Interval Scheduling 
utilizando backtracking.

- Sea charlas la lista de charlas ordenadas por hora de finalizacion ascendente.
- Sea Parcial una lista con las charlas que formen la solucion parcial.
- Sea Optima una lista con todas las charlas que formen la solucion optima.

Comienzo llamando para la charla que termina primero, por ende no habrá charlas anteriores, cada vez que evalue una charla me fijo si la puedo agregar, osea si no se solapa con
la ultima, en caso afirmativo la agrego y si mejoré la cantidad óptima actualizo tal optimo y llamo para la próxima charla si no puedo agregarla simplemente llamo para la proxima charla.
Termino cuando ya no quedan charlas por evaluar. El arbol tendrá a lo sumo n nodos significando que todas las charlas no se solapan, en cada nodo del arbol se realiza un trabajo de
- Validación con la ultima charla para ver si puedo agregar la actual.
- Comparación de cantidades en solucion parcial y optima para ver si encontre una mejor solucion.

El arbol tendrá hasta 2^n nodos dado que podemos incluir o no a un elemento, la complejidad temporal es O(n log n) + O(2^n) por lo tanto finalmente será O(2^n). La complejidad espacial
será a lo sumo O(n) si todas las charlas son compatibles.
'''

# Constantes para las tuplas de charlas
INICIO = 0
FIN = 1

# Constantes para las estructuras parcial y opt
CHARLAS = 0
CANTIDAD = 1

def IntervalScheduling(charlas):
    charlas = sorted(charlas, key=lambda x: x[FIN])
    n = len(charlas)
    parcial = [[], 0]
    opt = [[], 0]
    i = 0
    IntervalSchedulingBt(charlas, n, parcial, opt, i)
    return opt[CHARLAS]

def IntervalSchedulingBt(charlas, n, parcial, opt, i):
    # Caso base: hemos evaluado todas las charlas
    if i >= n:
        return
    
    # Opción 1: Intentar incluir la charla actual
    if puedoAgregarEstaCharla(parcial, charlas[i]):
        parcial[CHARLAS].append(charlas[i])
        parcial[CANTIDAD] += 1
        
        # Si encontramos una mejor solución, actualizamos opt
        if parcial[CANTIDAD] > opt[CANTIDAD]:
            opt[CHARLAS] = parcial[CHARLAS].copy()
            opt[CANTIDAD] = parcial[CANTIDAD]
        
        # Llamada recursiva incluyendo la charla
        IntervalSchedulingBt(charlas, n, parcial, opt, i + 1)
        
        # Deshacemos el cambio (backtracking)
        parcial[CHARLAS].pop()
        parcial[CANTIDAD] -= 1
    
    # Opción 2: No incluir la charla actual
    IntervalSchedulingBt(charlas, n, parcial, opt, i + 1)

def puedoAgregarEstaCharla(parcial, charla):
    if not parcial[CHARLAS]:  # Si no hay charlas en la solución parcial
        return True
    return parcial[CHARLAS][-1][FIN] <= charla[INICIO]

'''
Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso (para ella)
que pueda y que entre en su mochila. Tiene 2 limitaciones. La primera: no puede guardar más peso que lo que permita su mochila (tiene límite hasta W). 
La segunda: como sabe que puede entrar en un estado de locura e inconciencia temporal, se puso un límite que no comprará por más de P precio en total
(es decir, la suma de todo lo comprado). Cada producto tiene 3 valores asociados: 
su valor (vi, que Laura definió en base a su subjetividad), su precio (pi) y su peso (wi).
Implementar un algoritmo que, utilizando programación dinámica, permita determinar qué productos debe comprar Laura tal que no superen el peso máximo 
que puede llevar y el precio máximo dispuesto a pagar, y que logre maximizar el valor obtenido (dados por la suma de los elementos comprados).
También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado.

Este es un caso tipico del problema de la mochila, buscamos ir agregando productos en función de maximizar el valor que Laura les da a los mismos, para esto,
dado un producto y un peso podemos ingresar el mismo a la mochila considerando que pueden haber otros en la misma que ya estén ocupando cierto peso y por lo cual
el valor de dichos productos que ya se encuentran en la mochila se sumarán al de este en caso de poder hacerlo. También es posible que dado un producto P el mismo
pese lo mismo que los que ya se encuentren en la mochila o que una parte de ellos mientras que pueden estar dicho producto y otros más (es decir saco algunos productos, dejo otros
que ya estaban y agrego el que estoy evaluando actualmente). Para calcular los óptimos de manera incremental (y secuencial) la idea es "ir agrandando el peso maximo de la mochila a
medida que agrego elementos" ,es decir, al contemplar un nuevo elemento pruebo de agregarlo con peso 1, luego con peso 2, luego con peso 3 y así hasta W. Al mismo tiempo, cuando pueda
ingresar un elemento debo también evaluar no quedarme sin dinero, por lo tanto tenemos que calcularemos el óptimo del elemento "i" para el peso maximo "w":

    Opt[i][w] = max( Vi + Opt[i][W-Wi][P-Pi], Opt[i-1][W][P] ) es decir incluir el item o no incluirlo y considerar el optimo calculado para el elemento anterior.
    
La complejidad temporal al construir los óptimos es O(n * w * p) con n la cantidad de productos, w el peso maximo y p el presupuesto maximo. Dado que al final para reconstruir la solución
se recorre al revés, la complejidad temporal total resulta en la misma al igual que la complejidad espacial por el uso de memoria en dicha matriz de tres dimensiones.
'''

# Entrada:
# - productos: lista de tuplas (valor, peso, precio) = [(v_i, w_i, p_i)]
# - W: peso máximo
# - P: precio máximo

def MochilaPokemon(productos, W, P):
    n = len(productos)
    
    # dp[i][w][p] = valor máximo considerando los primeros i ítems,
    # con peso máximo w y precio máximo p
    dp = [[[0 for p in range(P + 1)] for w in range(W + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        # i-1 es el índice del ítem actual en la lista productos
        v_i = productos[i-1][0]  # Valor del ítem i
        w_i = productos[i-1][1]  # Peso del ítem i
        p_i = productos[i-1][2]  # Precio del ítem i
        
        for w in range(W + 1):
            for p in range(P + 1):
                if w_i <= w and p_i <= p:
                    dp[i][w][p] = max(dp[i-1][w][p], v_i + dp[i-1][w - w_i][p - p_i])
    
    # Reconstrucción de la solución
    sol = []
    w_restante = W
    p_restante = P
    for i in range(n, 0, -1):
        # Si el valor cambió al incluir el ítem i, significa que lo tomamos
        if dp[i][w_restante][p_restante] != dp[i-1][w_restante][p_restante]:
            sol.append(i-1)  # Agregamos el ítem i-1 a la solución
            w_restante -= productos[i-1][1]
            p_restante -= productos[i-1][2]
    
    # Devolvemos el valor máximo y la lista de ítems (índices)
    return dp[n][W][P], sol