'''
12
------------------------------------------------------------------------------------------------------------------------------------
Tenemos como entrada una lista con elementos de la forma (dia_inicio, dia_fin) de largo N la cual ordenaremos por día de inicio.
Posteriormente guardaremos la primera en el arreglo resultante y comenzamos a iterar la lista ordenada a partir del segundo elemento.
Sabemos por el órden establecido que el rango actual no pudo haber empezado antes aunque si pudo haber empezado el mismo día y terminar luego que el
anterior previamente agregado en el arreglo resultante.

Si el rango actual comienza en el mismo dia que el ultimo agregado y termina mas tarde entonces el actual reemplaza al ultimo agregado.
Si el rango actual no comienza en el mismo dia que el ultimo agregado y termina mas tarde entonces lo agregamos.
Si el rango actual termina antes que el ultimo agregado entonces lo salteamos.

La complejidad temporal es O(n log n) debido al ordenamiento, la complejidad espacial es O(n).
'''