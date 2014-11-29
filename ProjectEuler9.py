#!/usr/bin/python
"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from random import randint
from math import sqrt

global a,b
b = randint(1,1000)
a = randint(1,b)


while type(sqrt(a**2 + b**2)) != type(2) and (a + b + sqrt(a**2 + b**2) !=1000):
	b = randint(1,1000)
	a = randint(1,b)

print(a*b*sqrt(a**2 + b**2),a,b,sqrt(a**2 + b**2))
