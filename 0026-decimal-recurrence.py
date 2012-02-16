"""
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
def traditional():
    # Initialization
    start = 2
    limit = 1000
    max_num = 1
    max_cycle = 1

    # Refer http://en.wikipedia.org/wiki/Repeating_decimal for the supporting logic
    for d in range(start, limit+1):
        # Getting the recurrence length
        n = 1
        while n < d:
            x = 10**n - 1
            if x % d == 0:
                break
            n += 1
        # If n is not equal to d, then there is a recurrence
        if n != d:
            if n > max_cycle:
                max_cycle = n
                max_num = d

    return max_num, max_cycle

print "Answer:", traditional()
