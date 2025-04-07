'''
⭐ Un ramal ferroviaria pone en concesión los patios de comida en todas las estaciones.
Son en total “n” estaciones. Por cada estación se cuenta con el promedio de facturación de los últimos 5 años.
Por normativa antimonopólica existe como limitante que ninguna empresa puede explotar 3 o más estaciones contiguas.
Pero, no existe una cantidad máxima de estaciones a explotar. Un oferente nos solicita que le digamos cuales son 
las estaciones que le conviene obtener para maximizar sus ganancias.
Plantee la solución mediante programación dinámica.

Dado un arreglo de longitud N que cuenta en cada posición con el promedio de facturación de los últimos 5 años de tal
estación (cada indice lo vamos a pensar como una estación en el órden de un ramal el cual comienza en estaciones[0])
tenemos como restricción que a lo sumo podemos tener dos estaciones contiguas elegidas pero no más. Para el caso de la primera
estación el óptimo hasta aquí será claramente elegir esta estación, y para el caso de la segunda el óptimo es elegir a la primera
y a esta misma. Pensemos en el caso general a partir de la tercera estación, si elegimos obtener la concesión de la estación I
entonces no podemos considerar el óptimo de la estación I - 1 pero sí el de la estación I - 2 dado que de esta forma no tendríamos
3 estaciones contiguas.
Dicho esto tenemos como casos base:
 - Opt[0] = estaciones[0]
 - Opt[1] = estaciones[0] + estaciones[1]
Y como caso general a partir de i = 3:
 - Opt[i] = max(opt[i-1], opt[i-2] + estaciones[i])
Luego, para reconstruir las elecciones comenzamos desde la última estación I, si Opt[I] = Opt[i-2] + estaciones[i] la agregamos, sino
seguimos.

Complejidad temporal O(n) iteramos el arreglo para calcular los óptimos al igual que para luego reconstruir la solución.
Complejidad espacial O(n) por el arreglo de óptimos.
'''

def concesiones_optimas(estaciones):
    n = len(estaciones)
    opt = [None for _ in range(n)]
    
    opt[0] = estaciones[0]
    opt[1] = estaciones[0] + estaciones[1]
    
    # Construímos los óptimos.
    for i in range(2, n):
        opt[i] = max(opt[i-1], opt[i-2] + estaciones[i])
    
    # Reconstruímos las elecciones.
    i = n - 1
    res = []
    while i >= 0:
        if opt[i] == opt[i-2] +  estaciones[i]:
            res.append(i)
            i -= 2
        else:
            i -= 1

    # Se debe agregar también la primera estación.
    if i == i:
        res.append(0)

    res.reverse()
    return res

# ramal = [Constitucion, Yrigoyen, Avellaneda, Sarandí, Domínico, Wilde, Don Bosco, Bernal, Quilmes]
estaciones_promedios = [
    5.5, # 0 - Constitucion
    0.1, # 1 - Yrigoyen
    2.3, # 2 - Avellaneda
    0.0, # 3 - Sarandí
    0.3, # 4 - Domínico
    0.3, # 5 - Wilde
    0.2, # 6 - Don Bosco
    0.1, # 7 - Bernal
    1.2  # 8 - Quilmes
]

print(concesiones_optimas(estaciones_promedios))