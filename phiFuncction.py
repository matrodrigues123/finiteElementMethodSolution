def phi(x,L):
    phie1 = 2*(x/L)**3 - 3*(x/L)**2 + 1
    phie2 = x**3/L**2 -2*x**2/L + x
    phie3 = -2*(x/L)**3 + 3*(x/L)**2
    phie4 = x**3/L**2 -x**2/L

    return phie1, phie2, phie3, phie4

def phiDoubleDot(x, L):
    phieDD1 = 12*x/L**3 - 6/L**2
    phieDD2 = 6*x/L**2 -  4/L
    phieDD3 = -12*x/L**3 + 6/L**2
    phieDD4 = 6*x/L**2 -2/L

    return phieDD1, phieDD2, phieDD3, phieDD4