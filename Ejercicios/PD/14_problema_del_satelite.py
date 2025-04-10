'''
⭐ Para un nuevo satélite a poner en órbita una empresa privada puede optar por incluir diversos sensores a bordo
(por ejemplo: variación de temperatura, humedad en tierra, caudal de ríos, etc). Cada uno de ellos tiene un peso "pi" 
y una ganancia "gi" calculado por su uso durante la vida útil del satélite. Si bien les gustaría incluir todos, el 
satélite tiene una carga máxima P que puede llevar. Nos piden que generemos un algoritmo (utilizando programación dinámica) 
para resolver el problema. Indique si su solución es polinomial.

Este caso es el problema de la mochila, lo que haremos es ir agregando sensores a medida que incrementamos el peso tolerado
hasta llegar a P, de modo que memorizaremos los óptimos para cada elemento y cada peso P máximo hasta haber evaluado todos los
sensores hasta un peso P. De esta forma guardaremos los óptimos en una matriz de NxP con N la cantidad de sensores y P el peso
que soporta el satélite. Si un sensor de peso W es posible agregarlo para el peso Pi actual (con 0 <= Pi <= P) entonces compararemos:
    - La ganancia que nos da ese sensor más la ganancia memorizada para el peso Pi - Wi.
    - La ganancia que nos da agregar ese sensor para el peso Pi.
'''
PESO = 0
GANANCIA = 1

def problema_del_satelite(sensores, P):
    n = len(sensores)
    opt = [[0 for _ in range(P+1)] for _ in range(n+1)]

    # Construimos la matriz de óptimos
    for i in range(1, n+1):
        Wi = sensores[i-1][PESO]
        Gi = sensores[i-1][GANANCIA]
        for j in range(P+1):
            if j >= Wi:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j - Wi] + Gi)
            else:
                opt[i][j] = opt[i-1][j]

    # Reconstrucción de la solución
    res = []
    i, j = n, P
    while i > 0 and j > 0:
        Wi = sensores[i-1][PESO]
        Gi = sensores[i-1][GANANCIA]
        if j >= Wi and opt[i][j] == opt[i-1][j - Wi] + Gi:
            res.append(sensores[i-1])
            j -= Wi
        i -= 1

    res.reverse()
    return res

sensores = [
    (2, 40),  # peso = 2, ganancia = 40
    (3, 50),  # peso = 3, ganancia = 50
    (4, 65),  # peso = 4, ganancia = 65
    (5, 85),  # peso = 5, ganancia = 85
    (9, 150)  # peso = 9, ganancia = 150
]
P = 10  # capacidad máxima de carga del satélite

print(problema_del_satelite(sensores, P))