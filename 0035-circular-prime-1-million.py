"""
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""
import math
from collections import deque

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
    start = 2
    end = 1000000
    
    done = {}
    
    # get all the primes from start to end
    primes = [x for x in enumerate_primes(end)]
    circular_prime_counter = 0
    
    for i in primes:
        if i in done:
            continue
            
        done[i] = True
            
        num_str = deque(str(i))
        
        count = 0
        
        for x in range(len(num_str)):
            # right circular shift
            num_str.rotate(1)
            
            num = int(''.join(num_str))
            
            if num in primes or num in done:
                done[num] = True
                count = count + 1
            else:
                break
        
        if count == len(num_str):
            circular_prime_counter = circular_prime_counter + count
    
    return circular_prime_counter
    
print "Answer by usual method:", the_usual_method()
