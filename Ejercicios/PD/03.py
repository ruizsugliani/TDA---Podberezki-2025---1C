'''
⭐ El dueño de una empresa desea organizar una fiesta de la misma. Cómo quiere que la fiesta sea 
lo más tranquila posible, no quiere que asistan un empleado y su jefe directo. Pidió a su encargado 
que le ponga un rating de convivencia (Ri) a cada empleado. Con dicha información más un organigrama 
de la compañía, le pidió a un especialista en informática que diseñe un algoritmo para obtener el 
listado de los empleados que deberá invitar a la fiesta. Teniendo en cuenta que: Ri > 0, que no 
cuenta para el armado del algoritmo y que la estructura jerárquica es en forma de árbol. 
Se pide resolver mediante programación dinámica.
'''
def organizar_fiesta(G, ratings, s):
    vertices = G.obtener_vertices()
    padre = {v: None for v in vertices}
    abuelo = {v: None for v in vertices}
    opt = {v: None for v in vertices}
    
    for v in vertices:
        for w in G.adyacentes(v):
            padre[w] = v
    
    for v in vertices:
        abuelo[v] = padre[padre[v]]
    
    opt[s] = ratings[s]
    for v in vertices:
        opt[v] = max(opt.get(abuelo[v], 0) + ratings[v], opt.get(padre[v]))
    
    return opt