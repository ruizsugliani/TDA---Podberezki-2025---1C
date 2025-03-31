'''
Un conjunto de “n” personas votó de forma anónima entre un conjunto de “o” opciones (con o<<n).
El resultado de la votación lo tenemos en un vector de n posiciones ordenado por opción seleccionada.
Queremos determinar cuántos votos tuvo cada una de las opciones.
Podemos hacerlo simplemente recorriendo el vector en O(n). 
Sin embargo, utilizando división y conquista se puede lograr en un tiempo inferior.
Presentar y analizar una solución utilizando división y conquista que logre lo solicitado.
'''

def cant_votos(votos, o):
    return _cant_votos(votos, 0, len(votos) - 1)

def _cant_votos(votos, ini, fin):
    if fin <= ini:
        return {votos[ini]: 1}
    
    m = (ini + fin) // 2
    izq = _cant_votos(votos, ini, m)
    der = _cant_votos(votos, m + 1, fin)
    
    for key, value in der.items():
        izq[key] = izq.get(key, 0) + value
    return izq

print(cant_votos([0,0,0,0,1,1,2], 3))