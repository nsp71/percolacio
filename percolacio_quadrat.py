import matplotlib.pyplot as plt
import numpy as np
import random
from collections import deque

def matriu_quadrat(n,p):
    matriu = np.zeros((n,n),int)    #Comencem generant una matriu buida de dimensions nxn

    for i in range(n):
        for j in range(n):
            q = random.random() #Probabilitat de formar enllaç, si  q >= p es forma enllaç (1 a la matriu), altrament 0
            if q < p:
                matriu[i,j] = 1
    return matriu


#Esta función emplea el algoritmo bfs para encontrar caminos a partir de un punto dado.
#Devuelve un vector con los puntos de la matriz visitados
#Inici és una tupla de dos números que indiquen una posició dins la matriu.
def bfs(matriu, inici):
    visitat = np.zeros(matriu.shape, dtype=bool)
    queue = deque([inici])
    vertex_actius = []

    #Mientras queden elementos en la cola para ser explorados el bucle no para
    #El concepto de deque es una abstracción de estructura de datos que sigue el principio fifo.
    while queue:
        row, col = queue.popleft()
        visitat[row, col] = True

        if matriu[row,col] == 1:
            vertex_actius.append((row,col))

        # Obtener vecinos válidos no visitados
        for neighbor_row, neighbor_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            #amb la condició 0 <= ens assegurem que estem dins dels límits de la matriu.
            if 0 <= neighbor_row < len(matriu) and 0 <= neighbor_col < len(matriu[0]) and not visitat[neighbor_row, neighbor_col] and matriu[neighbor_row, neighbor_col] == 1:
                visitat[neighbor_row, neighbor_col] = True
                vertex_actius.append((neighbor_row,neighbor_col))
                queue.append((neighbor_row, neighbor_col))

    return vertex_actius


def percola(matriu):
    n = len(matriu)
    # Puntos alcanzables desde la parte superior e inferior respectivamente
    top_reachable = bfs(matriu, [0, 0])
    bottom_reachable = bfs(matriu, [n-1, 0])

    # Puntos alcanzables desde los laterales izquierdo y derecho respectivamente
    left_reachable = bfs(matriu, [0, 0])
    right_reachable = bfs(matriu, [0, n-1])

    # Comprobar si hay algún punto en ambos conjuntos para la parte superior e inferior
    for point in top_reachable:
        if point in bottom_reachable:
            return True  # Hay percolación

    # Comprobar si hay algún punto en ambos conjuntos para los laterales izquierdo y derecho
    for point in left_reachable:
        if point in right_reachable:
            return True  # Hay percolación

    return False  # No hay percolación

#Funció que donada una matriu i una llista de posicions, canvia els valors de les posicions donades per 2's
def pintar_cami(matriu,vertex_actius):

    matriu_pintada = matriu.copy()
    for i in vertex_actius:
        matriu_pintada[i] = 2
    return matriu_pintada


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#CODI PRINCIPAL

n = 5  #Mida de la matriu
p = 0.9 #Probablitat d'ocupació (la p del vèrtex ha de ser > p per formar enllaç)

matriu = matriu_quadrat(n,p)
vertex_actius = bfs(matriu, [0,0])


print(matriu)
print(percola(matriu))

if percola(matriu):
    matriu_pintada = pintar_cami(matriu,vertex_actius)
    print(matriu_pintada)

#TODO: Graficar percolación en función de las dimensiones de la matriz de 2x2 hasta 10x10 para empezar.










