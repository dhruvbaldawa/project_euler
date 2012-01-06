"""
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def the_old_fashioned_way():
    power = 5
    li = []
    # The following 2 variables are used to calculate the upper bound
    max_digits_to_check = 7
    max_number_per_digit = 9 ** power
    for i in range(2, max_digits_to_check * max_number_per_digit):
        l = [int(x) ** power for x in str(i)]
        if i == sum(l):
            li.append(i)
    ans = sum(li)
    return ans

print "Answer the old-fashioned way:", the_old_fashioned_way()
