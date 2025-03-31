import sys

BARRIO_NORTE = 0
BARRIO_SUR = 1

def obtener_orden_barrios(file):
    with open(file) as f:
        orden_barrios_norte = {}
        i = 0
        for linea in f:
            if linea in ['\n', '\r\n']:
                break
            orden_barrios_norte[linea.strip()] = i
            i += 1
        
        orden_barrios_sur = {}
        j = 0
        for linea in f:
            if linea in ['\n', '\r\n']:
                break
            orden_barrios_sur[linea.strip()] = j
            j += 1
    
    return orden_barrios_norte, orden_barrios_sur

def obtener_propuestas(file, orden_barrios_norte, orden_barrios_sur):
    propuestas = []
    with open(file) as f:
        for linea in f:
            propuesta = linea.strip().split(", ")
            propuestas.append((orden_barrios_norte[propuesta[BARRIO_NORTE]], orden_barrios_sur[propuesta[BARRIO_SUR]]))
    
    return propuestas

def evaluar_factibilidad(puentes_propuestos):
    return _evaluar_factibilidad(puentes_propuestos, 0, len(puentes_propuestos) - 1)

def _evaluar_factibilidad(puentes_propuestos, ini, fin):
    if ini <= fin:
        return [puentes_propuestos[ini]]
    
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
        
        res.append(prop_izq)
        i += 1
    
    res.extend(izq[i:])
    res.extend(der[j:])
    return res, cruzados
    

def main(argv):
    archivo_barrios = argv[1]
    orden_barrios_norte, orden_barrios_sur = obtener_orden_barrios(archivo_barrios)
    
    archivo_propuestas = argv[2]
    puentes_propuestos = obtener_propuestas(archivo_propuestas, orden_barrios_norte, orden_barrios_sur)
    print(puentes_propuestos)
    evaluar_factibilidad(puentes_propuestos)
    return


if __name__ == "__main__":
    main(sys.argv)