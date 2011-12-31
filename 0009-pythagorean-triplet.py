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
    """
    Checks whether a given number is a perfect square or not
    """
    return int(math.sqrt(n))**2 == n

def gcd(a, b):
    """
    Find GCD of two numbers a and b
    """
    if b==0:
        return a
    else:
        r=a%b
        return gcd(b,r)
         
def pythagorean():
    """
    The Brute-force method to find the triplet
    """
    # Building a list of perfect squares
    l = [x for x in range(2, 1000)]
    ans = 0
    
    for a in l:
        for b in l:
                c = 1000 - (a + b)
                if a**2 + b**2 - c**2  == 0:
                    # Here we have the answer (a, b, c)!
                    ans = a*b*c
    return ans

def optimized_pythagorean():
    """
    This is pure mathematical implementation, and direct simulation of equations.
    Hence, the variable names are mis-leading !
    """
    n = 1000
    # Dividing n by 2 ignoring repetitive iterations
    n2 = n/2
    mlimit = int(math.ceil(math.sqrt(n2))) - 1
    
    for m in range(2, mlimit):
        # Check if n2 is divisible by m
        if n2 % m == 0:
            nm = n2 / m
            
            # Remove all factors of 2
            while nm % 2 == 0:
                nm = nm / 2
            # If number is odd, increase by 2
            if m % 2 == 1:
                k = m + 2
            # If even, increment by 1
            else:
                k = m + 1
            # Refer pdf overview for supporting formulae and derivation
            while k < 2*m and k <= nm:
                if nm % k == 0 and gcd(k, m) == 1:
                    d = n2 / (k * m)
                    l = k - m
                    a = d * (m*m - l*l)
                    b = 2 * d * m * l
                    c = d * (m*m + l*l)
                    
                    # The answer is (a, b, c)
                    return a*b*c
                k = k + 2

print "Answer by traditional method:", pythagorean()
print "Answer by optimized method:", optimized_pythagorean()
