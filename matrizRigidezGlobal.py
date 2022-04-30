import numpy as np

def matrizRigidezLocal(E, I, L):
    return E*I*np.array([
        [12/L**3,  6/L**2, -12/L**3,  6/L**2],
        [6/L**2,   4/L,     -6/L**2,  2/L],
        [-12/L**3, -6/L**2, 12/L**3, -6/L**2],
        [6/L**2,   2/L,     -6/L**2,  4/L]])

def matrizRigidezGlobal(a, b, c, d, e, f, g, I, E):
    ## Inicializando matriz global
    kg = np.zeros((10,10))

    ## Elementos
    # Elemento 1 (1,2)
    L1  = a + b
    ke1 = matrizRigidezLocal(E,I,L1)
    kg[0:4, 0:4] += ke1

    # Elemento 2 (2,3)
    L2  = c
    ke2 = matrizRigidezLocal(E,I,L2)
    kg[2:6, 2:6] += ke2

    # Elemento 3 (3,4)
    L3  = d + e + f
    ke3 = matrizRigidezLocal(E,I,L3)
    kg[4:8, 4:8] += ke3

    # Elemento 4 (4,5)
    L4  = g
    ke4 = matrizRigidezLocal(E,I,L4)
    kg[6:10, 6:10] += ke4

    # Aplicando as condições de contorno
    kg[0, :] = kg[:, 0] = kg[4, :] = kg[:, 4] = kg[8, :] = kg[:, 8] = np.zeros(10)
    kg[0,0] = kg[4,4] = kg[8,8] = 1
    
    return kg










