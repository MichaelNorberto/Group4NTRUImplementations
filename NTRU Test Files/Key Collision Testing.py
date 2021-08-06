import sympy as sym
from sympy import GF
import secrets
import time

N = 157
p = 3
q = 127

overallTime = 0.0
overallList = []
for i in range(1,50):
    t0 = time.time()
    mutationRate = 0.4
    fList = []
    gList = []
    def generateF(N):
        for i in range (0,N):
            threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
            if threshold >= 0.5:
                if threshold <= mutationRate:
                    fList.append(-1)
                fList.append(1)
            elif threshold < 0.5:
                if threshold <= mutationRate:
                    fList.append(-1)
                fList.append(0)
        return fList

    for i in range (0,N):
        threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
        if threshold >= 0.5:
            if threshold <= mutationRate:
                gList.append(-1)
            gList.append(1)
        elif threshold < 0.5:
            if threshold <= mutationRate:
                gList.append(-1)
            gList.append(0)
    #############################################################
    def make_poly(N, coeffs):

        x = sym.Symbol('x')
        coeffs = list(reversed(coeffs))
        y = 0
        if len(coeffs) < N:
            for i in range(len(coeffs)):
                y += (x**i)*coeffs[i]
            y = sym.poly(y)
            return y
        else:
            for i in range(N):
                y += (x**i)*coeffs[i]
            y = sym.poly(y)
            return y

    f = generateF(N)
    g = gList


    f_poly = make_poly(N,f)
    g_poly = make_poly(N,g)


    x = sym.Symbol('x')

    while True:
        try:
            Fp = sym.polys.polytools.invert(f_poly,x**N-1, auto=True, domain=GF(p, symmetric = False))
            break
        except:
            print("Found Non Invertible Polynomial. Regenerating Polynomial.....\n")
            try:
                f = generateF(N)
                f_poly = make_poly(N,f)
                Fp = sym.polys.polytools.invert(f_poly,x**N-1,auto = True, domain=GF(p, symmetric = False))
            except:
                print("Found Second Non Invertible Polynomial. Regenerating.....\n")
                try:
                    f = generateF(N)
                    f_poly = make_poly(N,f)
                    Fp = sym.polys.polytools.invert(f_poly,x**N-1,auto = True, domain=GF(p, symmetric = False))
                except:
                    print("Found Third Non Invertible Polynomial. Regenerating.....\n")
                    f = generateF(N)
                    f_poly = make_poly(N,f)
                    Fp = sym.polys.polytools.invert(f_poly,x**N-1,auto = True, domain=GF(p, symmetric = False))
        else:
            f = generateF(N)
            f_poly = make_poly(N,f)
            Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric = False))
    Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric = False))

    h = p*((Fq.mul(g_poly)))

    h = sym.polys.polytools.trunc(h, q)
    hCoeffs = h.coeffs()
    s = ''.join(str(hCoeffs))
    overallList.append(s)
    

    t1 = time.time()
    total = t1 - t0
    overallTime = overallTime + total
    average = overallTime / i
    print("\nPublic Key = ", h)
    print("\nThe time to generate keys was: ", total, "s")
    print("The average time to generate keys was: ", average, "s")
    
setList = set(overallList)
duplicate = len(overallList) != len(setList)
if duplicate == True:
    print("There are duplicate keys in the set ")
else:
    print("There are no duplicates in the set, duplicates = ", duplicate)
