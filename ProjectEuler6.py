#!/usr/bin/python
"""


The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def somme(n):
    liste1 = [i**2 for i in range(n+1)]
    liste2 = [i for i in range(n+1)]
    return (sum(liste2))**2 - sum(liste1)

print(somme(100))
