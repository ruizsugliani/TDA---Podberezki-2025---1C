'''
A raíz de una nueva regulación industrial un fabricante debe rotular cada lote que produce según un valor numérico que lo caracteriza. 
Cada lote está conformado por “n” piezas. A cada una de ellas se le realiza una medición de volumen. La regulación considera que el lote
es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el rótulo deberá ser ese valor. De lo contrario el lote 
se descarta. 

Actualmente cuenta con el proceso “A” que consiste en para cada pieza del lote contar cuántas de las restantes tienen el mismo volumen. 
Si alguna de las piezas corresponde al “elemento mayoritario”, lo rotula. De lo contrario lo rechaza. 

Un consultor informático impulsa una solución (proceso “B”) que considera la más eficiente: ordenar las piezas por volumen y con ello 
luego reducir el tiempo de búsqueda del elemento mayoritario.

Nos contratan para construir una solución mejor (proceso “C”). Se pide: 
a) Exprese mediante pseudocódigo el proceso “A”.
b) Explique si la sugerencia del consultor (proceso “B”) realmente puede mejorar el proceso. En caso afirmativo, arme el pseudocódigo que lo ilustre.
c) Proponga el proceso “C” como un algoritmo superador mediante división y conquista. Explíquelo detalladamente y brinde pseudocódigo.
'''

def proceso_a(lote):
    cant_piezas = len(lote)
    vol_piezas = {} # Guardamos en un diccionario la cantidad de piezas de volumen K.
    for vol in lote: # Iteramos los volúmenes del lote, donde por cada volúmen incrementamos en uno la cantidad de elementos con el mismo.
        if vol not in vol_piezas:
            vol_piezas[vol] = 0
        else:
            vol_piezas[vol] += 1

    elem_mayor = None
    for vol in vol_piezas.keys(): # Buscamos si algun volumen es mayoritario y en tal caso lo devolvemos
        if vol_piezas[vol] >= cant_piezas // 2:
            elem_mayor = vol
            break
        
    return elem_mayor # La complejidad es O(n)

# Mediante la sugerencia del proceso B no es posible meorar la complejidad dado que el ordenamiento ya impone la complejidad O(n log n) siendo esta peor que la del proceso A.

# Haciendo uso de división y conquista podríamos dado el arreglo pasado por parámetro con los volúmenes de los elementos en el lote, llamar recursivamente para cada mitad del arreglo
# actual hasta llegar al caso base de un elemento, posteriormente al momento de conquistar queremos quedarnos con el volúmen que se repita más de la mitad de las veces para el arreglo
# del llamado en cuestión. Tendremos entonces por cada nivel dos llamados recursivos para cada mitad del arreglo actual, cada uno de ellos nos dara un candidato el cual debemos evaluar
# si aparece más de la mitad de las veces en el arreglo actual, en tal caso devolverlo. Tenemos entonces A = 2, B = 2, f(n) = O(n). Por el teorema maestro la complejidad temporal es O(n log n)

def proceso_c(lote):
    n = len(lote) -  1
    return _proceso_c(lote, 0, n)

def _proceso_c(lote, ini, fin):
    if fin <= ini:
        return lote[ini]
    
    m = (ini + fin) // 2
    
    cand_izq = _proceso_c(lote, ini, m)
    cand_der = _proceso_c(lote, m + 1, fin)
    
    cant_apariciones_izq = 0
    cant_apariciones_der = 0
    
    for i in range(ini, fin + 1): # O(n)
        if lote[i] == cand_izq:
            cant_apariciones_izq += 1
        if lote[i] == cand_der:
            cant_apariciones_der += 1
    
    if cant_apariciones_izq > (fin - ini) // 2:
        return cand_izq
    
    if cant_apariciones_der > (fin - ini) // 2:
        return cand_der
    
    return None

print(proceso_c([2, 2, 3, 2]))