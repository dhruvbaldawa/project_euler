"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math

def get_optimized_prime(n):
    if n < 4:
        return n
    while n % 2 == 0 and n != 2 : n = n/2
    if n < 9:
        return n
    while n % 3 == 0 and n != 3 : n = n/3
    # Starting out with 3
    i = 5
    
    # Checking till the square root of n
    while i <= math.floor(math.sqrt(n)) :
        # Checking for divisibility with the ith number and reducing
        # n to reflect the divisibility
        while n % i == 0 and n != i:
            n = n / i
        # Increase i by 2, because the prime numbers are odd except for 2
        i = i + 2
    return n

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

def optimized():
    n = 2000000
    l = enumerate_primes(n)
    return sum(l)

def traditional():
    s = set()
    i = 3
    s.add(2)
    while True:
        p = get_optimized_prime(i)
        if p > 2000000:
            break
        s.add(p)
        i = i + 2
    #print s
    l = list(s)
    
    ans = reduce(lambda x,y: x + y, l)     
    return ans

print "Answer by traditional method:", traditional()
print "Answer by optimized method:", optimized()
