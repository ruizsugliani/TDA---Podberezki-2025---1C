BARRIO_NORTE = 0
BARRIO_SUR = 1

def evaluar_factibilidad(puentes_propuestos):
    return _evaluar_factibilidad(puentes_propuestos, 0, len(puentes_propuestos) - 1)

def _evaluar_factibilidad(puentes_propuestos, ini, fin):
    if fin <= ini:
        return [puentes_propuestos[ini]], 0
    
    m = (ini + fin) // 2
    
    izq, cruz_izq = _evaluar_factibilidad(puentes_propuestos, ini, m)
    der, cruz_der = _evaluar_factibilidad(puentes_propuestos, m + 1, fin)
    
    return merge_puentes(izq, der, cruz_izq + cruz_der)

def merge_puentes(izq, der, cruzados):
    i = j = 0
    res = []
    
    while i < len(izq) and j < len(der):
        prop_izq = izq[i]
        prop_der = der[j]
        
        if prop_izq[BARRIO_SUR] < prop_der[BARRIO_SUR] and prop_izq[BARRIO_NORTE] > prop_der[BARRIO_NORTE]:
            res.append(prop_der)
            j += 1
            cruzados += 1
            continue
        
        if prop_izq[BARRIO_SUR] > prop_der[BARRIO_SUR] and prop_izq[BARRIO_NORTE] < prop_der[BARRIO_NORTE]:
            res.append(prop_izq)
            i += 1
            cruzados += 1
            continue
        
        if prop_izq[BARRIO_NORTE] > prop_der[BARRIO_NORTE]:
            res.append(prop_der)
            j += 1
        else:
            res.append(prop_izq)
            i += 1
    
    res.extend(izq[i:])
    res.extend(der[j:])
    return res, cruzados

print(evaluar_factibilidad([(0, 1), (1, 2), (2, 0)]))
print(evaluar_factibilidad([(2, 0), (0, 1), (1, 2)]))
print(evaluar_factibilidad([(0, 1), (2, 0), (1, 2)]))
#print(evaluar_factibilidad([(0, 5),(4, 3), (0, 0), (2, 3), (1, 2), (3, 4)]))