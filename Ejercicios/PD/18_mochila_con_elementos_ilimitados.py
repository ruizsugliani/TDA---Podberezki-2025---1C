'''
⭐⭐ Una variante del problema de la mochila corresponde a la posibilidad de incluir una cantidad ilimitada de cada uno de los elementos disponibles.
En ese caso, tenemos una mochila de tamaño “k” y un conjunto de “n” elementos con stock ilimitado. Cada elemento tiene un peso y un costo. Queremos seleccionar
el subconjunto de elementos que maximice la ganancia de la mochila sin superar su capacidad. Solucione el problema utilizando programación dinámica.

En este caso del problema de la mochila, al poder agregar un elemento una ilimitada cantidad de veces debemos considerar si al evaluar ingresar un elemento
a la mochila me conviene:
    - Agregarlo y por ende tendría el costo de Ci + el costo obtenido para el peso P - Pi previamente calculado.
    - No agregarlo porque ya encontré que agregando elementos previamente evaluados conseguía una mayor ganancia.
    
Tenemos entonces que la ecuación de recurrencia es: Opt[N][P_act] = max(Opt[N][P_act-Pi] + Ci, Opt[N-1][P_act]) considerando que hay N elementos en la entrada de nuestro problema,
P_act es el peso actual considerado, Pi el peso del elemento y Ci el costo del mismo.
'''
PESO = 0
COSTO = 1

def mochila_con_elementos_ilimitados(elementos, K):
    n = len(elementos)
    opt = [[0 for _ in range(K+1)] for _ in range(n+1)] # Consideramos como caso base el caso sin elementos y los casos con K = 0.
    
    for i in range(1, n+1):
        for p in range(1, K+1):
            Ci = elementos[i-1][COSTO]
            Pi = elementos[i-1][PESO]
            
            if p >= Pi:
                opt[i][p] = max(opt[i][p-Pi] + Ci, opt[i-1][p])
            else:
                opt[i][p] = opt[i-1][p]

    res = []
    i, j = n, K
    while i > 0 and j > 0:
        Ci = elementos[i-1][COSTO]
        Pi = elementos[i-1][PESO]
        if j >= Pi and opt[i][j] == opt[i][j - Pi] + Ci:
            res.append(elementos[i-1])
            j -= Pi
        else:
            i -= 1
    
    res.reverse()
    return res, opt[n][K]

elementos = [
    (1, 15),   # peso 1, ganancia 15
    (3, 50),   # peso 3, ganancia 50
    (4, 60),   # peso 4, ganancia 60
    (5, 90)    # peso 5, ganancia 90
]

K = 8

print(mochila_con_elementos_ilimitados(elementos, K))