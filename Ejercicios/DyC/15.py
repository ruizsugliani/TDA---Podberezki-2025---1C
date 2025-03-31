'''
Dentro de un país existen dos colonias subacuáticas cada una de ellas con “n” habitantes.
Cada habitante tiene su documento de identidad único identificado por un número.
Para una tarea especial se decidió seleccionar a aquella persona que vive en alguna de
las colonias cuyo número de documento corresponda a la mediana de todos los números de
documento presentes en ellas. Por una cuestión de protocolo no nos quieren dar los listados
completos de documentos. Solo nos responden de cada colonia ante la consulta “Cual es el documento
en la posición X de todos los habitantes de la isla ordenados de mayor a menor”. Utilizando esto,
proponer un algoritmo utilizando división y conquista que resuelva el problema con la menor cantidad 
posibles de consultas. Analizar complejidad espacial y temporal.

Tenemos un pais con dos colonias, cada una de N habitantes, buscamos a la persona que vive en alguna de ellas dos
tal que su documento corresponda a la mediana de todos los números de documento presenten en estas colonias. Nuestro algoritmo
toma por parámetro la mediana y N (la cantidad de personas en cada colonia). Suponiendo que comenzamos por la colonia A vamos a preguntar
cuál es el documento en N//2 de dicha colonia:
    - Si el documento corresponde a la mediana encontramos el resultado.
    - Si el documento en N//2 es mayor tenemos que descartar hasta esa posición del arreglo inclusive y preguntamos para M = (N + N // 2) // 2
    - Si el documento en N//2 es menor tenemos que descartar desde esa posición del arreglo en adelante y preguntamos para M = (N - N // 2) // 2
    
Si volvemos a preguntar por la misma posición significa que el documento no se encuentra en dicha colonia y hay que repetir comenzando de nuevo desde N para la colonia B.
La complejidad temporal finalmente es O(2 * log n) = O(log n) mientas que la complejidad espacial es O(1).
'''