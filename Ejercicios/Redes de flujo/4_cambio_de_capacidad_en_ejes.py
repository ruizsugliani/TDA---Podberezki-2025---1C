'''
⭐⭐ Contamos con una red de Flujo definida sobre el grafo G=(V,E) y tenemos una asignación de flujo f(e) sobre G.
Nos solicitan elaborar un algoritmo que en base a esta información nos indique cómo se actualiza el flujo si uno de
los ejes tiene un cambio de capacidad (puede ser positiva o negativa). Debemos evitar volver a ejecutar el algoritmo
de Ford-Fulkerson desde cero. Explicar los diferentes casos que podrían suceder. Utilizar los conceptos de flujo máximo/corte
mínimo en su explicación. Brindar pseudocódigo de su propuesta y análisis de complejidad.

    - Si una arista (u, v) tiene f(u, v) = 0 tras modificar su capacidad entonces no se actualiza el flujo porque al haberse aplicado
    FF no se encontró un camino de aumento que la incluya.
    - Si un arista (u, v) tiene f(u,v) > 0 tras modificar su capacidad entonces:
        - Al ser un cambio en la capacidad donde se incrementa la capacidad original de la arista, si la misma era el cuello de botella de
        su camino de aumento, entonces el flujo incrementará (en caso de que aún con mayor capacidad siga siendo el cuello de botella).
        - Al ser un cambio en la capacidad donde se incrementa la capacidad original de la arista, si la misma no era el cuello de botella de
        su camino de aumento, entonces el flujo permanecerá igual.
        - Al ser un cambio en la capacidad donde se decrementa la capacidad original de la arista, si la misma era el cuello de botella de
        su camino de aumento, entonces el flujo decrementará.
        - Al ser un cambio en la capacidad donde se decrementa la capacidad original de la arista, si la misma no era el cuello de botella de
        su camino de aumento, entonces el flujo permanecerá igual (en caso de que aún con menor capacidad siga sin ser el cuello de botella).
    - Las aristas que formen parte del corte mínimo si ven aumentada su capacidad entonces aumentarán el flujo máximo y decrementarán el mismo en caso contrario.
'''