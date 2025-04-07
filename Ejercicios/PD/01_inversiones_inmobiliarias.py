'''
⭐ Para una inversión inmobiliaria un grupo inversor desea desarrollar un barrio privado paralelo a la una ruta.
Con ese motivo realizaron una evaluación de los diferentes terrenos en un trayecto de la misma. Diferentes 
inversores participarán, pero a condición de comprar algún terreno en particular. El grupo inversor determinó
para cada propiedad su evaluación de ganancia. El mismo surge como la suma de inversiones ofrecida por el 
terreno menos el costo de compra. Debemos recomendar que terrenos contiguos comprar para que maximicen sus
ganancias.  Ejemplo: S = [-2, 3, -3, 4, -1, 2]. La mayor ganancia es de 5, comprando los terrenos de valor
[4, -1, 2]. Solucionar el problema mediante un algoritmo de programación dinámica.

Opt(0) = max(0, S[0])
Opt(i) = max(0, Opt[i-1] + S[i])
'''
def inversiones_inmobiliarias(V):
    n = len(V)
    Opt = [None for _ in range(n)]
    Opt[0] = max(0, V[0])
    max_ganancia = 0
    ix_max_ganancia = 0
    
    for i in range(1, n):
        Opt[i] = max(0, Opt[i-1] + V[i])
        if Opt[i] > max_ganancia:
            max_ganancia = Opt[i]
            ix_max_ganancia = i
    
    j = ix_max_ganancia
    total = 0
    res = []
    while total != max_ganancia:
        total += V[j]
        res.append(V[j])
        j  -= 1
    res.reverse()
    
    return max_ganancia, res

print(inversiones_inmobiliarias([-2, 3, -3, 4, -1, 2]))
print(inversiones_inmobiliarias([-2, 10, -3, 4, 3, 2, -12]))