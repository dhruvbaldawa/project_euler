"""
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
def get_divisors(i, n = 2):
    """
    Recursive get divisors of a number
    """
    # Terminating condition, return 1
    if n > i**0.5:
        return [1]
    
    # If divisor
    if i % n == 0:
        if n != i/n:
            return_ = [n] + [i/n] + get_divisors(i, n + 1)
        else:
            return_ = [n] + get_divisors(i, n + 1)

        return return_
    # If not divisor
    else:
        return get_divisors(i, n + 1)

def is_abundant(n):
    """
    Checks whether a number abundant or not
    """
    l = get_divisors(n)
    return n < sum(l)

def the_obvious():
    start = 1
    end = 28123
    # create a list of abundant numbers
    abundant_numbers = [x for x in range(start, end + 1) if is_abundant(x)]
    
    # create a set of all numbers which are sum of 2 abundant numbers
    s = set()
    for x in abundant_numbers:
        for y in abundant_numbers:
            if x + y <= end:
                s.add(x + y)
    
    # minus this set from the set of positive integers and find its sum !
    answer = sum(set(range(start, end + 1)) - s)
    
    return answer

print "Answer:", the_obvious()
