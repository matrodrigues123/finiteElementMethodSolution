import numpy as np
from parameters import *
from matrizRigidezGlobal import matrizRigidezGlobal
from phiFuncction import phi, phiDoubleDot

## Resolver o sistema 
kg = matrizRigidezGlobal(a, b, c, d, e, f, g, I, E)
fg = np.array([V1, M1, V2, M2, V3, M3, V4, M4, V5, M5])
ug = np.linalg.solve(kg, fg)

## Deslocamentos em cada ponto
# Ponto  1
[phie1,phie2,phie3,phie4] = phi(a, a+b);
v1 = ug[0]*phie1 + ug[1]*phie2 + ug[2]*phie3 + ug[3]*phie4 

# Ponto 2
[phie1,phie2,phie3,phie4] = phi(d, d+e+f);
v2 = ug[4]*phie1 + ug[5]*phie2 + ug[6]*phie3 + ug[7]*phie4

# Extensometro
[phieDD1,phieDD2,phieDD3,phieDD4] = phiDoubleDot(d+e, d+e+f)
v3DD = ug[4]*phieDD1 + ug[5]*phieDD2 + ug[6]*phieDD3 + ug[7]*phieDD4

## Resultados
resultM3 = E*I*v3DD
sigma = -(10**(-3))*resultM3*(altura/2)/I;
e3 = (sigma/E)*10**9
v1 = v1*10**3
v2 = v2*10**3

print(f'delta1 = {v1} mm\n')
print(f'delta2 = {v2} mm\n')
print(f'epsilon = {e3} um/m\n')
print(f'sigma = {sigma} kpa\n')

