#!/usr/bin/python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt


def nombre_premier(n):
    racine = int(sqrt(n))
    for i in range(2,racine+1):
        if n%i==0 and n!=i:
            return False
    return True

def premier():
    n = 3
    p = []
    while n <= 2000000:
        if nombre_premier(n) == True:
            p.append(n)
            n += 2
        else:
            n += 2
    return p

def somme():
    liste = [2]
    liste = premier()
    return sum(liste)

print(somme()) 
