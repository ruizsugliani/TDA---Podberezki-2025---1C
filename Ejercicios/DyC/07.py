'''
Para la elaboración de un juego se desea construir un cielo nocturno de una ciudad donde se vea el contorno de los edificios en el horizonte.
Cada edificio “ei“ está representado por rectángulos mediante la tripla (izquierda, altura, derecha).
Dónde “izquierda” corresponde a la coordenada x menor, “derecha” la coordenada x mayor y altura la coordenada y.
Todos los edificios inician en la coordenada 0 de y. 
Se cuenta con una lista de N edificios que llegan sin un criterio de orden específico. 
Se desea emitir como resultado el contorno representado como una lista de coordenadas “x” y sus alturas.
Tenga en cuenta el siguiente ejemplo:
Lista de edificios: (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16) , (14, 3, 25), (19,18,22).
Contorno: (1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(25,0).
Presentar un algoritmo utilizando división y conquista que dado el listado de edificios retorna como resultado el contorno de la ciudad.

Nuestro algoritmo toma como argumento una lista E de edificios de la forma:
    - (izquierda, altura, derecha)
Dado que buscamos los vértices que permitan dibujar el contorno de estos tenemos dos casos:
    - Dos edificios se "solapan", es decir si tenemos Ei, Ej entonces
        Ei_derecha >= Ej_izquierda
    - Dos edificios no se solapan y entonces
        Ei_derecha < Ej_izquierda
        
¿Cómo operamos en cada caso?
    - Si se solapan entonces agregamos:
        (Ei_izquierda, Ei_altura)
        (Ei_derecha, Ei_altura) si Ei_altura > Ej_altura sino (Ej_izquierda, Ej_altura), (Ej_derecha, Ej_altura)
        
    - Si no se solapan entonces podemos agregar el inicio y fin de cada uno, es decir, la solución al subproblema es:
        (Ei_izquierda, Ei_altura), (Ei_derecha, Ei_altura), (Ej_izquierda, Ej_altura), (Ej_derecha, Ej_altura)
        
¿Cómo operamos al juntar soluciones?
    Dado que hacemos un llamado recursivo para una mitad del arreglo y para la otra, los resultados de las mismas serán sus contornos.
    Lo que buscamos acá es algo asi como un merge
'''
X = IZQ = 0
ALT = 1
DER = 2

def contorno_edificios(E):
    e_ordenados = sorted(E, key=lambda x: x[0]) # ordenados por izquierda ascendente    ->  O(n log n) con n la cantidad de edificios
    return _contorno_edificios(e_ordenados, 0, len(e_ordenados) - 1)

def _contorno_edificios(E, ini, fin):
    if fin <= ini:
        ei = E[ini]
        ei_izq, ei_alt, ei_der = ei[IZQ], ei[ALT], ei[DER]
        return [(ei_izq, ei_alt), (ei_der, 0)]
    
    m = (ini + fin) // 2
    edificios_izq = _contorno_edificios(E, ini, m)
    edificios_der = _contorno_edificios(E, m + 1, fin)
    
    return merge_edificios(edificios_izq, edificios_der)

def merge_edificios(edificios_izq, edificios_der):
    res = []
    i = j = 0
    
    while i < len(edificios_izq) and j < len(edificios_der):
        ei = edificios_izq[i]
        ej = edificios_der[j]
        
        if ei[X] < ej[X]: # El edificio izquierdo comienza antes que el derecho, lo agrego si o si.
            res.append(ei)
            i += 1
        elif ei[X] > ej[X]: # El edificio derecho comienza antes que el izquierdo, lo agrego si o si.
            res.append(ej)
            j += 1
        else:
            if ei[ALT] >= ej[ALT]:
                res.append(ei)
            else:
                res.append(ej)
            i += 1
            j += 1
    
    while i < len(edificios_izq):
        ei = edificios_izq[i]
        if not res:
            res.append(ei)
        else:
            if res[-1][X] < ei[X]:
                res.append(ei)
        i += 1
            
    while j < len(edificios_der):
        ej = edificios_der[j]
        if not res:
            res.append(ej)
        else:
            if res[-1][X] < ej[X]:
                res.append(ej)
        j += 1
    
    return res

#print(contorno_edificios([(1, 11, 5), (2, 6, 7)]))
print(contorno_edificios([(1, 11, 5), (2, 6, 7), (3, 13, 9)]))