"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

def is_perfect_square(n):
    return int(math.sqrt(n))**2 == n

def pythagorean():
    # Building a list of perfect squares
    l = [x for x in range(2, 1000)]
    ans = 0
    
    for a in l:
        for b in l:
                c = 1000 - (a + b)
                if a**2 + b**2 - c**2  == 0:
                    ans = a*b*c
    return ans

print "Answer by traditional method:", pythagorean()
