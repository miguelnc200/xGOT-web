import pandas as pd
import numpy as np


# Coordenadas de la portería
x_goal = np.linspace(30.34, 37.66, 100)  # Anchura de la portería (x)
z_goal = np.linspace(0, 2.44, 50)        # Altura de la portería (z)
x_grid, z_grid = np.meshgrid(x_goal, z_goal)
y_goal = 0  # Coordenada Y constante (0)

# Función para calcular xGOT
def calculate_xgot(d_p, d_gb, d_0):
    return np.minimum(1, (d_p + d_gb) / d_0)
def calculated_gb(A,B,P):
    """
    Calcula la distancia del punto P a la recta definida por los puntos A y B
    """
    A = np.array(A)
    B = np.array(B)
    P = np.array(P)

    AB = B - A
    AP = P - A

    # Producto vectorial
    cross = np.cross(AB, AP)

    # Norma del producto vectorial dividido por la norma de AB
    distancia = np.linalg.norm(cross) / np.linalg.norm(AB)
    return distancia
# Calcular distancias y agregar columna xGOT
def compute_xgot_modified( balon_pos, portero_pos, end_pos):
    indices_a_eliminar = []
    try:
        d_0 = np.linalg.norm(balon_pos - portero_pos)
        if portero_pos[0] >60:
            pos_portero_final = [120,portero_pos[1],portero_pos[2]]
            d_p = np.linalg.norm(120 - portero_pos[0])
        else:
            d_p = np.linalg.norm(0 - portero_pos[0])
        d_gb = calculated_gb(balon_pos,end_pos,portero_pos)
    except Exception as e:
           d_p=0 
           d_gb=0
           d_0=0
   
    xgot = calculate_xgot(d_p, d_gb, d_0)
    return xgot  # Tomar el promedio como valor representativo