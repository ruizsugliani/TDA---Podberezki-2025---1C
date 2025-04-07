'''
⭐ Contamos con una carretera de longitud M km que tiene distribuidos varios carteles publicitarios.
Cada cartel ”i” está ubicado en un “ki” kilómetro determinado (pueden ubicarse en cualquier posición 
o fracción de kilómetro) y a quien lo utiliza le asegura una ganancia “gi”. Por una regulación no se
puede contratar más de 1 cartel a 5km de otros. Queremos determinar qué carteles conviene contratar 
de tal forma de maximizar la ganancia a obtener.

Tenemos como input un arreglo de tuplas de la forma (k, g), supongamos que estas tuplas vienen ordenadas
por k de forma ascendente. Vamos a recorrer este arreglo contabilizando el óptimo para la posición en i a
medida que iteramos. Tenemos como caso particular el del primer cartel, el cual su óptimo será considerarse a sí mismo.
Para el caso, general siendo que estamos analizando la optimalidad para el cartel en la posición J sabemos que los J - 1
carteles anteriores ya vieron calculada su optimalidad, debemos considerar que:
    - Si elegimos contratar este cartel, aquellos carteles anteriores con ubicación a menos de 5km de distancia de J no
    podrán ser considerados. Por lo tanto, si lo hacemos vamos a considerar la ganancia de ubicar este cartel J más la mayor
    ganancia óptima que aporte algún cartel anterior (ya calculada). Si uno de los carteles anteriores ubicados antes de los 5km
    dela regulación cuentan con un óptimo mayor, entonces lo tomamos como óptimo de J, lo cual se traduce a que el Opt[j-1] es mayor.
Obtenemos entonces que:
    - Opt[0] = V[0][GANANCIA]
    - Opt[j] = max(Opt[j-1])

La complejidad temporal es O(N^2) debido a la búsqueda del cartel anterior al actual a una distancia de al menos 5km, recorremos todos los carteles
y en cada caso buscamos el cartel anterior óptimo, luego en la reconstrucción la complejidad es O(N) debido al uso de indices realizando comparaciones O(1)
y decrementando el índice utilizado para ello. Mientras que la complejidad espacial es de O(2*N) dado que tenemos el arreglo de óptimos de longitud N y al mismo tiempo
el arreglo con los índices del cartel anterior "compatible" utilizado para cada caso.

'''
KI = 0
GI = 1

def optimalidad_carteles(carteles):
    n = len(carteles)
    opt = [None for _ in range(n)]
    elec_ant = [None for _ in range(n)]
    
    opt[0] = carteles[0][GI]
    ult_cartel = 0
    
    # Construímos los óptimos.
    for i in range(1, n):
        max_opt = 0
        
        for j in range(i):
            if carteles[i][KI] - carteles[j][KI] < 5:
                break
            if carteles[j][GI] > max_opt:
                max_opt = opt[j]
                elec_ant[i] = j
                
        if max_opt + carteles[i][GI] > opt[i-1]:
            opt[i] = max_opt + carteles[i][GI]
            ult_cartel = i
        else:
            opt[i] = opt[i-1]
    
    # Reconstruímos la solución.
    i = ult_cartel
    res = []
    while i is not None:
        res.append(carteles[i])
        i = elec_ant[i]
        
    res.reverse()
    return res

print(optimalidad_carteles([(2, 1), (3, 2), (4, 3), (7, 4), (8, 5)]))