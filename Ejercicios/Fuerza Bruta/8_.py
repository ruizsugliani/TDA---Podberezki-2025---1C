'''
⭐ Un granjero debe trasladar un lobo, una cabra y una zanahoria a la otra margen de un río.
Cuenta con un bote donde solo entra él y un elemento más. El problema es que no puede quedar solo el lobo y la cabra.
Dado que la primera se comería a la segunda. De igual manera, tampoco puede dejar solo a la cabra y la zanahoria.
La primera no dudaría en comerse a la segunda. ¿Cómo puede hacer para cruzar? Explicar cómo construir el grafo de estados del problema.
Determinar cómo explorarlo para conseguir la respuesta al problema. Brinde, si existe, la respuesta al problema.

Debido a las restricciones del problema sabemos que como primer viaje hacia la orilla final el granjero puede ir con la cabra (dejando al lobo y la zanahoria)
en la orilla inicial lo cual no dará problemas, posteriormente el granjero deberá volver a la orilla inicial y elegir un nuevo objeto. En nuestro arbol cada nodo tendrá
dos arreglos, el primero representando los que se quedan de la orilla inicial y el segundo los que se quedan en la orilla final. Nuestro primer nodo será de la forma:

oInicial = [G, L, C, Z]
oFinal = []

Según lo mencionado, por cada viaje ambas cambiarán, por ejemplo si en el primer viaje:

oInicial = [C, Z]
oFinal = [G, L]

Observaremos que en la orilla inicial la cabra se come a la zanahoria y por ende no es un estado válido a diferencia de un primer viaje que deje las orillas así:

oInicial = [L, Z]
oFinal = [G, C]

En el tercer viaje a partir de este nodo el granjero puede volver solo o con la zanahoria...

Sea oInicial = [G, L, C, Z] y oFinal = []
Sea posicionGranjero la orilla donde se encuentra (1 inicial, 2 final)
Sea crucesTotales una lista vacía con los cruces totales = []

Cruces(oInicial, oFinal, posicionGranjero)
    Si oFinal == [G, L, C, Z]
        Retornar crucesTotales
    
    Si posicionGranjero == 1
        Si HayConflictoEnOrilla(oFinal)
            Retornar Falso
        
    Si posicionGranjero == 2
        Si HayConflictoEnOrilla(oInicial)
            Retornar Falso
    
    
'''