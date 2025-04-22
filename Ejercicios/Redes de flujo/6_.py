'''
⭐⭐ Para un evento solidario un conjunto de n personas se ofrecieron a colaborar. En el evento hay m tareas a desarrollar.
Cada tarea tiene un cupo máximo de personas que la puede realizar. A su vez cada persona tiene ciertas habilidades que la hacen
adecuadas para un subconjunto de tareas. Proponga una solución mediante red de flujos que maximice la cantidad de personas asignadas
a las tareas. ¿Hay forma de lograr asegurarnos un piso mínimo de personas en cada tarea? ¿Cómo impacta en la solución presentada en el punto anterior?

Modelaremos el problema mediante una red de flujos y posteriormente aplicaremos FF para obtener el flujo máximo que equivaldrá a la cantidad máxima de
personas asignadas a tareas. Construiremos la red de flujo de la siguiente manera:
    - Unimos S a cada una de las N personas mediante una arista de capacidad M (con M la cantidad de tareas a desarrollar).
    - Unimos cada una de las N personas a las tareas que puedan desarrollar con una arista de capacidad 1
'''