'''
Todos los años la asociación de un importante deporte individual profesional realiza una preclasificación 
de los n jugadores que terminaron en las mejores posiciones del ranking para un evento exclusivo.
En la tarjeta de invitación adjuntan el número de posición en la que está actualmente y a cuantos
rivales invitados superó en el ranking comparado el año pasado. Contamos con un listado que tiene
el nombre del jugador y la posición del ranking del año pasado ordenado por el ranking actual. 
Ejemplo: LISTA: A,3 | B,4 | C,2 | D,8 | E,6 | F,5. Se puede ver que el jugador “A” superó al 
jugador “C”. El jugador “B” superó al jugador “C”. El jugador “C” no superó a ninguno de los invitados. Etc.
Proponer una solución utilizando la metodología de división y conquista.

Nuestra propuesta se basa en dividir el arreglo del nivel actual en 2 partes y resolver para cada mitad de forma recursiva,
posteriormente mergeamos ambas mitades contabilizando los rivales superados en cada caso. Si el participante de la mitad derecha
salio mejor rankeado antes que el dela izquierda, significa que el de la izquierda lo pasó. El caso base es cuando nuestro arreglo tiene
un solo elemento.
'''
JUGADOR = 0
POS_ANT = 1

def adelantos_ranking(lista):
    adelantos = {}
    for (player , _) in lista:
        adelantos[player] = 0
    merge_sort_modificado (lista, adelantos)
    return adelantos

def merge_sort_modificado (arr , adelantos):
    if len(arr) <= 1:
        return arr
    medio = len (arr) // 2
    izq = merge_sort_modificado (arr[:medio], adelantos)
    der = merge_sort_modificado (arr[medio:], adelantos)
    return merge_conteo(izq, der, adelantos)

def merge_conteo(arr1, arr2, set_adelantos):
    i = 0
    j = 0
    nuevo = []
    while i < len(arr1) and j < len(arr2) :
        if arr1[i][POS_ANT] <= arr2[j][POS_ANT]:
            nuevo.append(arr1[i])
            i += 1
        else:
            nuevo.append(arr2[j])
            set_adelantos[arr1[i][0]] += len(arr1) - i
            j += 1
    nuevo.extend(arr1[i:])
    nuevo.extend(arr2[j:])
    return nuevo

print(adelantos_ranking([("A", 3), ("B", 4), ("C", 2), ("D",8), ("E",6), ("F",5)]))