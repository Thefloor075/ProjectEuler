"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from math import *

def problem32():

    s = 0

    for i in range(10000):
        for j in range(10000):
            b = i*j
            if problem(b,i,j) == True:
                print(b,i,j)
                s += b
    return s



def problem(b,i,j):

    L = []
    
    x = str(i)
    y = str(j)
    z = str(b)

    dfg = len(x) + len(y) + len(z)

    if dfg < 9 or dfg > 9:
        return False
    else:
        for k in range(len(x)):
            L.append(int(x[k]))
        for k in range(len(y)):
            L.append(int(y[k]))
        for k in range(len(z)):
            L.append(int(z[k]))

    B = [1,2,3,4,5,6,7,8,9]

    for i in range(len(L)):
        if L[i] not in B:
            return False
        else:
            B.remove(L[i])
    return True

print(problem32())
