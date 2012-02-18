"""
Problem 27

Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2  79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for
consecutive values of n, starting with n = 0.
"""
import math
def enumerate_primes(n): 
    if n == 2: return [2]
    elif n < 2: return []
    s = range(3,n+1,2)
    nroot = math.sqrt(n)
    half=(n+1)/2 - 1
    i = 0
    m = 3
    while m <= nroot:
        if s[i]:
            j = (m*m-3)/2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m=2 * i + 3
    return [2] + [x for x in s if x]

def is_prime(n):
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def traditional():
    limit = 1000
    # b must be a prime, for n = 0
    b_list = enumerate_primes(limit)
    # Initialization
    max_ = 0
    max_ab = (0,0)

    for b in b_list:
        # Checking for a in the limit specified
        for a in range(1, limit):
            # Check for a
            n = 0
            while True:
                t = n**2 + a*n + b
                if is_prime(t):
                    n += 1
                else:
                    break
            if n > max_:
                max_ = n
                max_ab = (a, b)

            if a < b:
                # Check for -a
                n = 0
                while True:
                    t = n**2 - a*n + b
                    if is_prime(t):
                        n += 1
                    else:
                        break
                if n > max_:
                    max_ = n
                    max_ab = (-a, b)

    return max_, max_ab, max_ab[0] * max_ab[1]
print "Answer:", traditional()
