"""
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
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

cache = {}
primes_cache = {}
def get_recursive_prime_factors(n):
    global cache
    # Performance enhancement (memoization)
    if n in cache:
        return cache[n]
    # Get the list of primes
    primes = enumerate_primes(int(math.sqrt(n)) + 1)
    l = []
    # If the list of primes is empty, return
    if not primes:
        cache[n] = l
        return cache[n]
    # Checking for divisibility by primes
    for prime in primes:
        # If divisible by a prime
        if n % prime == 0:
            l.append(prime)
            cache[n] = l + get_prime_factors(n/prime)
            return cache[n]
        # If n < current_prime, it is surely not divisible
        # so, just return the residue l
        if prime > math.sqrt(n):
            cache[n] = l
            return cache[n]
        # If n is prime, it will not be divisible, so return n
        if is_prime(n):
            l.append(n)
            cache[n] = l
            return cache[n]
    cache[n] = l
    return cache[n]

def get_prime_factors(n):
    if n == 1:
        return []
    l = []
    # Factorize the powers of 2
    while n % 2 == 0:
        l.append(2)
        n //= 2
    
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            l.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        l.append(n)
    return l

def traditional():
    # Initialization
    start = 100
    i = start
    count = 0 # Count of numbers with the specified number of prime factors
    latest = [] # The list of numbers
    max_count = 4 # The maximum number of consecutive numbers
    n_factors = 4 # THe maximum number of prime factors

    while True:
        # If the count is reached, end !
        if count >= max_count:
            #l = l[-4:-1]
            break
        # Get the number of prime factors
        n_prime_factors = len(set(get_prime_factors(i)))
        
        # If the number of prime factors is satisfied
        if n_prime_factors == n_factors:
            count += 1
            latest.append(i)
        else:
            count = 0
            latest = []
        i += 1
    
    return latest

print "Answer:", traditional()
