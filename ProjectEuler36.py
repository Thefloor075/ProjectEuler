"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def somme():
    n,s = 1,0
    while n < 999999:
        if palindromes(n) == True:
            s += n
            n += 1
        else:   n += 1
    return s

def palindromes(n):
    binary = bin(n)
    binary = binary[2:]
    n = str(n)
    if n == n[::-1] and binary == binary[::-1]:    return True
    else:    return False


print(somme())
