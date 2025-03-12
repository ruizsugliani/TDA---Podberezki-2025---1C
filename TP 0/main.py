import sys
from collections import deque

def main(argv):
    archivo = argv[1]
    pilas = deque()
    
    with open(archivo) as f:
        for linea in f:
            carta_actual = int(linea.strip())
            apilada = False

            for p in pilas:
                tope = p[-1]
                if tope > carta_actual:
                    p.append(carta_actual)
                    apilada = True
                    break
            
            if not apilada:
                nueva_pila = deque([carta_actual])
                pilas.append(nueva_pila)
                
    print(len(pilas))

if __name__ == "__main__":
    main(sys.argv)