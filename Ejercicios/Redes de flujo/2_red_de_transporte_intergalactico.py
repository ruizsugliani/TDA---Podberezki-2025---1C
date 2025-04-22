'''
⭐ La red de transporte intergaláctico es una de las maravillas del nuevo imperio terráqueo.
Cada tramo de rutas galácticas tiene una capacidad infinita de transporte entre ciertos planetas. 
No obstante, por burocracia - que es algo que no los enorgullece - existen puestos de control en cada
planeta que reduce cuantos naves espaciales pueden pasar por día por ella. Por una catástrofe en el planeta X,
la tierra debe enviar la mayor cantidad posible de naves de ayuda. Por un arreglo, durante un día los planetas
solo procesaran en los puestos de control aquellas naves enviadas para esta misión.  Tenemos que determinar cuál 
es la cantidad máxima de naves que podemos enviar desde la tierra hasta el planeta X.
Sugerencia: considerar a este un problema de flujo con capacidad en nodos y no en ejes

En este caso tenemos la red de flujo, donde el nodo S es la tierra, los nodos conmutadores los planetas intermedios entre
la tierra y el planeta X, y finalmente el planeta X es el nodo T de nuestra red. Como dato tenemos que cada tramo entre planetas
tiene una capacidad infinita, por lo tanto de primeras todas las aristas tienen dicha capacidad, pero tamibén tenemos como dato la
cantidad de naves que puede pasar por cada planeta en un día. Es por esto que modificaremos la red, de modo que para todo nodo conmutador J
crearemos un nuevo nodo J' y uniremos J -> J' con una capacidad igual al dato para dicho planeta, de este modo al aplicar FF se irán colapsando
dichas aristas hasta obtener el flujo máximo s - t (para este caso Tierra - Planeta X).
'''