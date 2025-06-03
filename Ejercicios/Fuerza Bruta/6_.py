'''
⭐⭐ Contamos con un conjunto de “n” actividades entre las que se puede optar por realizar.
Cada actividad x tiene una fecha de inicio Ix, una fecha de finalización Fx y un valor Vx que obtenemos por realizarla.
Queremos seleccionar el subconjunto de actividades compatibles entre sí que maximice la ganancia a obtener 
(suma de los valores del subconjunto). Proponer un algoritmo por branch and bound que resuelva el problema.

En nuestro arbol de decisión nuestro nodo inicial contará con 0 actividades seleccionadas, sabemos que a lo sumo dicho arbol
tendrá una profundidad de "n" nodos en el caso de ser todas las actividades compatibles entre sí. Inicialmente consideraremos que
nuestra mejorSolucion = [] y valorMejorSolucion = 0, ya que buscamos maximizar este último. En este caso la propiedad de corte se basa
en que las actividades seleccionadas sean compatibles entre sí, para esto en un primer momento vamos a ordenar las actividades según su 
fecha de finalización de forma que al agregar una nueva al subconjunto, si la misma es compatible a la anterior (la última agregada al subconjunto)
entonces se supera la propiedad de corte. La función costo se determina según el estado I como el valor alcanzado en tal estado I más el valor más alto
dentro de las próximas actividades multiplicado por la cantidad de actividades restantes, constituyendo entonces una cota superior, definimos entonces que
FC = maximoValorActividadProx * (N - I).

Sea actividades el arreglo de actividades de la forma (Ix, Fx, Vx) de largo "n".
Sea (inicialmente) mejorSolucion = [] el arreglo con el subconjunto de actividades que constituyen la mejor solución.
Sea (inicialmente) valorMejorSolucion = 0 la sumatoria de los valores de las actividades que constituyen la mejor solución.

HallarMejoresActividades(act)
    actividades = ordenar act según Fx ascendente
    n = largo de act
    mejorSolucion = []
    valorMejorSolucion = 0
    solucionParcial = []
    valorSolucionParcial = 0
    
    BranchAndBound(actividades, i, n, mejorSolucion, valorMejorSolucion, solucionParcial, valorSolucionParcial)
    
    Retornar mejorSolucion, solucionParcial

BranchAndBound(actividades, i, n, mejorSolucion, valorMejorSolucion, solucionParcial, valorSolucionParcial)
    // Caso base: se procesaron todas las actividades.
    Si i >= n:
        Si valorSolucionParcial > valorMejorSolucion:
            valorMejorSolucion = valorSolucionParcial
            mejorSolucion = solucionParcial
        Retornar mejorSolucion, valorMejorSolucion
    
    // Caso poda: no vamos a hallar una mejor solución.
    cota = valorSolucionParcial + FC(actividades, solucionParcial, i, n)
    Si cota <= valorMejorSolucion:
        Retornar mejorSolucion, valorMejorSolucion
    
    // Agregamos la actividad actual si podemos
    actividadActual = actividades[i]
    Si esCompatible(solucionParcial, ActividadActual)
        solucionParcial.append(ActividadActual)
        valorSolucionParcial += ActividadActual[Vx]
        mejorSolucion, valorMejorSolucion = BranchAndBound(actividades, i+1, n, mejorSolucion, valorMejorSolucion, solucionParcial, valorSolucionParcial)   
        solucionParcial.pop()
        valorSolucionParcial -= ActividadActual[Vx]

    mejorSolucion, valorMejorSolucion = BranchAndBound(actividades, i+1, n, mejorSolucion, valorMejorSolucion, solucionParcial, valorSolucionParcial)
    Retornar mejorSolucion, valorMejorSolucion

FC(actividades, solucionParcial, i, n)
    // Cota superior: suma de valores de actividades compatibles restantes
    valorCota = 0
    ultimaActividad = solucionParcial[-1] si tiene elementos, sino None
    Para j = i hasta n-1:
        Si esCompatible(ultimaActividad, actividades[j]):
            valorCota += actividades[j][Vx]
            ultimaActividad = actividades[j]
    Retornar valorCota

esCompatible(actividadesAnteriores, actividadActual)
    Si actividadesAnteriores == [] o actividadesAnteriores es None:
        Retornar Verdadero
    Retornar actividadesAnteriores[Fx] <= actividadActual[Ix]
'''