"""
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math
from collections import deque
from copy import copy

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
    start = 7
    end = 800000
    
    # get all the primes from start to end
    primes = [x for x in enumerate_primes(end)]
    # counting 2 as prime
    truncatable_primes = []
    
    for i in primes:            
        if i == 2 or i == 3 or i == 5 or i == 7:
            continue
        
        num_str = deque(str(i))
        
        count = 1
        # checking from left-to-right
        l = copy(num_str)
        while True:
            l.popleft()
            
            if len(l) == 0:
                break
                
            temp = ''.join(l)
            num = int(temp)
            if num in primes:
                count = count + 1
            else:
                break
                
        if count < len(num_str):
            continue
        
        count = 1
        # checking from right-to-left
        l = copy(num_str)
        while True:
            l.pop()
            
            if len(l) == 0:
                break
                
            temp = ''.join(l)
            num = int(temp)
            if num in primes:
                count = count + 1
            else:
                break
        
        if count == len(num_str):
            truncatable_primes.append(i)        
            
            
            
    return truncatable_primes
    
print "Answer by usual method:", the_usual_method()
