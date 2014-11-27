#!/usr/bin/python
"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def init():
    global a,b
    a = 0
    b = []

def recuperer_palindrome():
    for i in range(100,1000):
        for j in range(100,1000):                        
            a = i*j
            a = str(a)
            if a == a[::-1]:
                b.append(int(a))
        return b

def recuperer_max_palindrome():
    global pmax
    b = recuperer_palindrome()
    pmax = b[0]
    for i in range(len(b)):
        if b[i] > pmax:
            pmax = b[i]
    print(pmax)

pmax = 0
a = 0
b = []

init()
recuperer_max_palindrome()
