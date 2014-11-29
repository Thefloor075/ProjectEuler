#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

def diviseur(n):
        i = 1
        while n!= 1:
                if n%i == 0:
                        n /= i
                        i += 1
                else:   i += 1
        return i-1

print(diviseur(600851475143))
