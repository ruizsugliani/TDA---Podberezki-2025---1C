'''
04
------------------------------------------------------------------------------------------------------------------------------------
Contamos con:
    - m salas de conferencias.
    - n oradores.
Suponiendo que el input es una lista de elementos de la forma (hora_inicio, duración) y que debe haber 15 minutos entre charlas
vamos a transformar cada elemento de la lista pasada por parámetro y modificaremos el último elemento en cada uno con la hora_fin que se calculará
con hora_inicio + duracion + 15 minutos para modelar esos 15 minutos entre charla y charla. Luego ordenaremos estas charlas por hora_fin (osea priorizamos
las que terminan primero) y finalmente comenzaremos a recorrer el arreglo desde la segunda charla, ya que la primera charla le asignaremos el primer orador (n = 1).
Por cada orador vamos a ir contabilizando la hora en la cual termina de dar una charla al asignarlo a una. Al recorrer las charlas vamos a recorrer desde [1, n] y revisar
si dicho orador tiene una charla asignada, en caso de no tenerlo lo asignamos a la charla actual y le completamos cuando terminaria de darla, pero en caso de tener una charla lo asignaremos
solo si el horario de fin de esa charla es menor o igual al inicio de la charla actual. También llevaremos contabilizada en una variable la cantidad de salas utilizadas dado que cuando asignemos un
orador que no fue asignado antes a una nueva conferencia, significa que los anteriores se encuentran dando charlas y este nuevo orador debe dar la charla en una nueva sala.
Finalmente si recorremos los n oradores y todos estaban asignados, entonces el algoritmo termina.
Tenemos como complejidad temporal O(n*m) + O(k log k) dado el ordenamiento, el calculo de la hora de fin para cada charla y la revision de los oradores disponibles al iterar las charlas.
La complejidad espacial es O(n) por contabilizar cuando termina una charla cada orador (puede ser un dict).
'''