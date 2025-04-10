'''
⭐ Se proyectó la construcción de una línea de tensión eléctrica. En su trayecto pasa cerca de “n” ciudades que tienen diferentes demandas de consumo eléctrico.
Para la interconexión entre la línea y una central se debe construir una nexo. Por cuestiones regulatorias y constructivas no se pueden construir nexos a menos
de “x” kilómetros entre sí. Contamos con el listado de las ciudades. Para cada ciudad nos informan su población y la ubicación en la línea del nexo a construir.
Mediante programación dinámica proponga una solución que permita seleccionar qué ciudades conectar para maximizar la cantidad total de población cubierta por esta
línea.

Tenemos como entrada una lista con tuplas que representan ciudades representadas por (poblacion, ubicacion) donde para dicha ubicación se buscará agregar un nexo,
por otro lado, no podemos ubicar nexos a menos de X kilometros entre sí. Para la primera ciudad no hay ciudades antes, con lo cual Opt[0] = ciudades[POBLACION] 
representará construir el nexo en dicha ciudad. Para el caso general nos interesa cubrir una mayor cantidad de población que para el caso anterior, por lo tanto
dada la ciudad "i" verificaremos las "j" ciudades anteriores a esta, si la ubicación de "j" es a >= distancia X de "i" entonces contemplamos el óptimo de "j" más
la población de "i" para el óptimo de "j", también contemplaremos solo la población de "i" que puede ser mayor a la alcanzada por el óptimo de "j".

Tenemos entonces como ecuación de recurrencia:
Caso base       ->  Opt[0] = ciudades[0][POBLACION]
Caso general    ->  Opt[i] = max(ciudades[i][POBLACION], max(opt[j]) + ciudades[i][POBLACION], max(opt[k])) con j < i una ciudad previa a distancia al menos X, con k < i una ciudad previa a distancia menor a X.
'''
UBICACION = 0
POBLACION = 1

def poblacion_cubierta_optima(ciudades, X):
    N = len(ciudades)
    opt = [c[POBLACION] for c in ciudades]
    ant = [-1 for _ in ciudades]
    incluido = [True for _ in ciudades]  # marca si la ciudad fue seleccionada o no

    # Construcción del óptimo.
    for i in range(1, N):
        for j in range(i):
            distancia = ciudades[i][UBICACION] - ciudades[j][UBICACION]
            if distancia >= X and opt[j] + ciudades[i][POBLACION] > opt[i]:
                opt[i] = opt[j] + ciudades[i][POBLACION]
                ant[i] = j
                incluido[i] = True
            elif distancia < X and opt[j] > opt[i]:
                opt[i] = opt[j]
                ant[i] = j
                incluido[i] = False

    # Buscar el índice con el mayor valor óptimo
    max_idx = max(range(N), key=lambda i: opt[i])

    # Reconstrucción de la solución.
    res = []
    i = max_idx
    while i != -1:
        if incluido[i]:
            res.append(ciudades[i])
        i = ant[i]

    res.reverse()
    return res, opt[-1]

ciudades = [
    (2, 1000),   # Ciudad a 2 km, 1000 habitantes
    (5, 800),    # Ciudad a 5 km, 800 habitantes
    (7, 1200),   # Ciudad a 7 km, 1200 habitantes
    (10, 2000),  # Ciudad a 10 km, 2000 habitantes
    (14, 1500),  # Ciudad a 14 km, 1500 habitantes
    (17, 900),   # Ciudad a 17 km, 900 habitantes
    (20, 1800),  # Ciudad a 20 km, 1800 habitantes
]
x = 4  # Distancia mínima entre nexos

print(poblacion_cubierta_optima(ciudades, x))