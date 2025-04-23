'''
⭐⭐ Para un evento solidario un conjunto de n personas se ofrecieron a colaborar. En el evento hay m tareas a desarrollar.
Cada tarea tiene un cupo máximo de personas que la puede realizar. A su vez cada persona tiene ciertas habilidades que la hacen
adecuadas para un subconjunto de tareas. Proponga una solución mediante red de flujos que maximice la cantidad de personas asignadas
a las tareas. ¿Hay forma de lograr asegurarnos un piso mínimo de personas en cada tarea? ¿Cómo impacta en la solución presentada en el punto anterior?

Modelaremos el problema mediante una red de flujos y posteriormente aplicaremos FF para obtener el flujo máximo que equivaldrá a la cantidad máxima de
personas asignadas a tareas. Construiremos la red de flujo de la siguiente manera:
    - Unimos S a cada una de las N personas mediante una arista de capacidad 1 (cada persona puede realizar una sola tarea).
    - Unimos cada una de las N personas a un nodo T_p que habrá por cada persona, lo utilizaremos para saber si el mismo está o no asignado al aplicar FF,
    la capacidad de la arista será 1.
    - Unimos cada nodo T_p con todas las tareas que pueda realizar dicha persona con una arista de capacidad 1.
    - Finalmente unimos cada tarea con T con una arista de capacidad C igual al cupo máximo que permite tal tarea
'''
from ..utils import grafo as Grafo
# personas es un dict con clave nombre de la persona y valor una lista de las tareas que puede hacer.
# tareas es un dict con clave nombre de la tarea y valor su cupo maximo de personas a ser asignadas.
def armar_red_de_flujo(personas, tareas):
    red_flujo = Grafo(dirigido=True)
    
    # Creamos los nodos S y T
    red_flujo.agregar_vertice("S")
    red_flujo.agregar_vertice("T")
    
    # Creamos los nodos de tareas y los unimos a T.
    for t in tareas:
        red_flujo.agregar_vertice(t)
        red_flujo.agregar_arista(t, "T", tareas[t])
    
    # Creamos los nodos de tareas y los unimos a T.
    for p in personas:
        red_flujo.agregar_vertice(p)
        red_flujo.agregar_vertice(f"T_{p}")
        red_flujo.agregar_arista("S", p, 1)
        red_flujo.agregar_arista(p, f"T_{p}", 1)
        for t_posible in personas[p]:
            red_flujo.agregar_arista(f"T_{p}", t_posible, 1)
    
    return red_flujo

def obtener_asignaciones(red, personas):
    flujos, Gr = red.ford_fulkerson()
    asignaciones = []
    
    for p in personas:
        for ady in red.adyacentes(f"T_{p}"):
            if flujos[(f"T_{p}", ady)] == 1:
                asignaciones.append((p, ady))
                break
    
    return asignaciones
        