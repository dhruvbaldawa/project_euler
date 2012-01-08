"""
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import math
from itertools import permutations

def enumerate_primes(n): 
    """
    Get all the prime numbers to n
    """
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

def the_usual_method():
    start = 1000
    end = 9999
    
    # get all the primes from start to end
    primes = [x for x in enumerate_primes(end) if x >= start]
    
    l = []
    
    for i in primes:
        num_str = str(i)
        # to check for repetition of digits
        #if len(num_str) != len(set(num_str)):
        #    continue
        
        # find the permutations of a given number
        prime_perms = permutations(str(i))
        # convert the permutation tuples to integers
        prime_perms = [int(''.join(x)) for x in prime_perms]
        # filter to select only the prime permutations
        prime_perms = filter(lambda x: x in primes, prime_perms)
        
        # check to have at least three prime permutations
        if len(prime_perms) >= 3:
            # checking for the arithmetic progression
            for term in permutations(prime_perms, 3):
                
                x,y,z = sorted(term)
            
                if x - y == y - z and x != y and y != z:
                    l.append((x,y,z))
                    break
    return set(l)
        
print "Answer by usual method:", the_usual_method()
