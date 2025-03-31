'''
01
------------------------------------------------------------------------------------------------------------------------------------
Tenemos un listado de la forma (pueblo, km) donde cada elemento representa una bifurcacion
hacia dicho pueblo sobre una ruta. Buscamos minimizar la cantidad de patrullas a ubicar tal que
todas las bifurcaciones tengan a lo sumo a 50km de distancia una patrulla disponible.
'''
KM = 1

def bifurcaciones(arr):  
    res = []
    ordenadas = sorted(arr, key=lambda x: x[1])
    km_actual = ordenadas[0]
    i = 1
    
    while i < len(ordenadas):
        posible_patrullero = ordenadas[i]
        if posible_patrullero[KM] - km_actual[KM] > 50:
            res.append(ordenadas[i-1])
            km_actual = ordenadas[i]
        i += 1
    
    if ordenadas[i-1][KM] - res[-1][KM] > 50:
        res.append(ordenadas[i-1])
        
    return res
            
print(bifurcaciones([("A", 50), ("B", 100), ("C", 150)]))
print(bifurcaciones([("A", 50), ("C", 150)]))
print(bifurcaciones([("Lez", 156), ("Cast", 185), ("Sev", 194), ("Guido", 249), ("Maipu", 270)]))
print(bifurcaciones([("Lez", 156), ("Cast", 185), ("Sev", 194), ("Guido", 249), ("Maipu", 270), ("???", 1270)]))