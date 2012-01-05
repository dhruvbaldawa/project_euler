"""
Problem 20

n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

cache = {}

def factorial(n):
    """
    Memoized recursive function for the above expression
    """
    if n in cache:
        return cache[n]
    if n == 1:
        cache[1] = 1
        return cache[1]
    else:
        cache[n] = n * factorial(n - 1)
        return cache[n]

def the_simple_method():
    number = 100
    ans = reduce(lambda x,y: int(x) + int(y), str(factorial(number)))
    return ans


print "Answer by simple chain method:", the_simple_method()
