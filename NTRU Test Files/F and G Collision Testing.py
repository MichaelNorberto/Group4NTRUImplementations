import sympy as sym
from sympy import GF
import secrets
import time

N = 157
p = 3
q = 127

overallTime = 0.0
overallList = []
overallListG = []
for i in range(1,100):
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
    
    

    def generateG(N):
        for i in range (0,N):
            threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
            if threshold >= 0.5:
                if threshold <= mutationRate:
                    gList.append(-1)
                gList.append(1)
            elif threshold < 0.5:
                if threshold <= mutationRate:
                    fList.append(-1)
                gList.append(0)
        return gList
    
    f = generateF(N)
    g = generateG(N)
    print(f)
    print(g)
    sG = ''.join(str(g))
    s = ''.join(str(f))
    overallList.append(s)
    overallListG.append(sG)
    
    t1 = time.time()
    total = t1 - t0

setList = set(overallList)
duplicate = len(overallList) != len(setList)
if duplicate == True:
    print("There are duplicates in the set")
else:
    print("There are not duplicates in the set for F, duplicate = ", duplicate)

setListG = set(overallListG)
duplicateG = len(overallListG) != len(setListG)

if duplicateG == True:
    print("There are duplicates in the set")
else:
    print("There are not duplicates in the set for G, duplicate = ", duplicateG)
    
