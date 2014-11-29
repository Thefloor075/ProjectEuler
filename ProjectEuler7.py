#!/usr/bin/python
"""


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt

def condition(n):
    racine = int(sqrt(n))
    for i in range(2,racine+1):
        if n%i==0 and n!=i:
            return False
    return True

def premier():
    n = 2
    p = []
    while len(p)!= 10001:
        if condition(n) == True:
            p.append(n)
            n += 1
        else:
            n += 1
    print(p[10000])

premier()
