"""
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

def traditional():
    limit = 1000000
    
    primes_list = enumerate_primes(limit)
    
    l = []
    max_ = 1
    max_prime = 2
    for i in range(1, len(primes_list)):
        for k in range(1, i + 1):
            for j in range(k, i + 1):
                if sum(primes_list[k:j]) == primes_list[i]:
                    if len(primes_list[k:j]) > max_:
                        max_ = len(primes_list[k:j])
                        max_prime = primes_list[i]
                    l.append(primes_list[i])

    return max_prime

    
print "Answer by traditional method:", traditional()
