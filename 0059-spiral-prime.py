"""

Starting with 1 and spiralling anticlockwise in the following way, a 
square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom 
right diagonal, but what is more interesting is that 8 out of the 13 
numbers lying along both diagonals are prime; that is, a ratio of 8/13 = 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the 
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""
import math
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


def the_brute_force_thought():
    n_primes = 0
    n_numbers = 1
    limit = 0.10

    i = 2
    while True:
        # Generates 5, 17, 37...
        x = i ** 2 + 1
        # Generates 3, 13, 31...
        y = x - i

        if is_prime(x):
            n_primes += 1
        if is_prime(y):
            n_primes += 1
        n_numbers += 2

        i += 1
        # Generates 9, 25, 49...
        x = i ** 2
        # Generates 7, 21, 43...
        y = x - i + 1
        if is_prime(x):
            n_primes += 1
        if is_prime(y):
            n_primes += 1
        n_numbers += 2

        if n_primes / float(n_numbers) < limit:
            break

        i += 1

    return i
print "Answer:", the_brute_force_thought()
