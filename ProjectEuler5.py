"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
def suite():
    i = 20
    while divisible(i) != True:
            i += 20
    return i

def divisible(a):
    p = [20,19,18,17,16,15,14,13,12,11]
    """p = list(range(1,21))
    liste2 = p[::-1]"""
    for element in p:
            if a%element != 0:      return False
    return True

print(suite())
