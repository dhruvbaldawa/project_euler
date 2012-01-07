"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Note: I have quite implementation of this algorithm, which is little different from the 
one given in the overview pdf, but has really good performance. Traditional is very slow.
"""
import math 
def get_prime(n):
    """
    Function to get the largest prime number dividing a certain number
    """
    # To factor out all the powers of 2
    while n % 2 == 0 and n != 2 : n = n/2
    
    # Starting out with 3
    i = 3
    
    # Checking till the square root of n
    while i < n and n / i > 0 :
        # Checking for divisibility with the ith number and reducing
        # n to reflect the divisibility
        while n % i == 0 and n != i:
            n = n / i
        # Increase i by 2, because the prime numbers are odd except for 2
        i = i + 2
    return n

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

def traditional():
    s = set()
    i = 3
    s.add(2)
    while len(s) < 10001:
        s.add(get_optimized_prime(i))
        i = i + 2
    #print s
    ans = max(s)     
    return ans

print "Answer by traditional method:", traditional()
