#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import sys


# In[10]:


# Función para ver qué nodo que no ha sido visitado, necesita ser visitado en el siguiente paso

def nodos_a_visitar():
  global visited_and_distance
  v = -10
  # Eligiendo el vértice con la mínima distancia
  for index in range(number_of_vertices):
    if visited_and_distance[index][0] == 0       and (v < 0 or visited_and_distance[index][1] <=       visited_and_distance[v][1]):
        v = index
  return v


# In[11]:


#Representado el grafico de nodos como una matriz

# En la matríz de vértices se vé qué NODOS se conectan con otros NODOS

#grafo =      A  B  C  D  E  F  G  H  I
          #A[[0, 1, 1, 0, 0, 0, 0, 0 ,0],
           #B[1, 0, 0, 0, 1, 1, 0, 0, 0],
           #C[1, 0, 0, 1, 1, 0, 0, 0, 0],
           #D[0, 0, 1, 0, 1, 0, 1, 0, 0],
           #E[0, 1, 1, 1, 0, 0, 1, 1, 0],
           #F[0, 1, 0, 0, 0, 0, 0, 1, 0],
           #G[0, 0, 0, 1, 1, 0, 0, 0, 1],
           #H[0, 0, 0, 0, 1, 1, 0, 0, 1],
           #I[0, 0, 0, 0, 0, 0, 1, 1, 0]]

vertices = [[0, 1, 1, 0, 0, 0, 0, 0 ,0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0]]

#En la matriz de ejes, se reemplaza 1 de la matríz de arriba por el valor que tiene la conexión entre los 2 NODOS

edges =    [[0, 5, 9, 0, 0, 0, 0, 0 ,0],
            [5, 0, 0, 0, 10, 7, 0, 0, 0],
            [9, 0, 0, 3, 5, 0, 0, 0, 0],
            [0, 0, 3, 0, 1, 0, 4, 0, 0],
            [0, 10, 5, 1, 0, 0, 4, 2, 0],
            [0, 7, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 4, 4, 0, 0, 0, 12],
            [0, 0, 0, 0, 2, 8, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 12, 6, 0]]




number_of_vertices = len(vertices[0])


# In[12]:


#El primer elemento de la lista nodovisitado_mas_distancia denota que el nodo ya ha sido visitado,
#El segundo valor representa el valor de la distancia al nodo fuente A

visited_and_distance = [[0, 0]]
for i in range(number_of_vertices-1):
  visited_and_distance.append([0, sys.maxsize])


# In[13]:


for vertex in range(number_of_vertices):
  # Se calcula los nodos a visitar
  to_visit = nodos_a_visitar()
  for neighbor_index in range(number_of_vertices):
    #Se calcula la nueva distancia para los nodos que no han sido visitado para el vertice elegido
    if vertices[to_visit][neighbor_index] == 1 and      visited_and_distance[neighbor_index][0] == 0:
      new_distance = visited_and_distance[to_visit][1]       + edges[to_visit][neighbor_index]
      if visited_and_distance[neighbor_index][1] > new_distance:
        visited_and_distance[neighbor_index][1] = new_distance
  visited_and_distance[to_visit][0] = 1


# In[8]:


i = 0 

# Imprimiendo los resultados     
for distance in visited_and_distance:
  print("El camino óptimo o la menor distancia del nodo ",chr(ord('a') + i),  " al nodo fuente A es:",distance[1])
  i = i + 1


# In[ ]:




