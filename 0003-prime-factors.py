"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
    
def get_prime(n):
    """
    Function to get the largest prime number dividing a certain number
    """
    # To factor out all the powers of 2
    while n % 2 == 0 and n != 2 : n = n/2
    
    # Starting out with 3
    i = 3
    
    # Checking till the square root of n
    while i < n ** 0.5:
        # Checking for divisibility with the ith number and reducing
        # n to reflect the divisibility
        if n % i == 0:
            n = n / i
        # Increase i by 2, because the prime numbers are odd except for 2
        i = i + 2
    return n 

def traditional():
    number = 600851475143
    return get_prime(number)
            
print "Answer from traditional way:",traditional()
