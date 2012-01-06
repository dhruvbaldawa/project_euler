"""
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial
    
def the_old_fashioned_way():
    li = []
    # The following 2 variables are used to calculate the upper bound
    max_digits_to_check = 6
    max_number_per_digit = factorial(9)
    
    for i in range(3, max_digits_to_check * max_number_per_digit):
        l = [factorial(int(x)) for x in str(i)]
        if i == sum(l):
            li.append(i)
    ans = sum(li)
    
    return ans

print "Answer the old-fashioned way:", the_old_fashioned_way()
