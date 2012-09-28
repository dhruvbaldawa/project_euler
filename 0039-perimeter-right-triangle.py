"""
http://projecteuler.net/problem=39
"""
import math

def gcd(a, b):
    """
    Find GCD of two numbers a and b
    """
    if b==0:
        return a
    else:
        r=a%b
        return gcd(b,r)

def optimized_pythagorean(n):
    """
    This is pure mathematical implementation, and direct simulation of equations.
    Hence, the variable names are mis-leading !
    """
    # Dividing n by 2 ignoring repetitive iterations
    n2 = n/2
    mlimit = int(math.ceil(math.sqrt(n2))) - 1
    count = 0
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
                    count += 1
                k = k + 2
    return count

def main():
    MAX = 1000
    return max(range(MAX), key=optimized_pythagorean)

print main()