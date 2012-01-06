"""
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
def traditional():
    start = 2
    limit = 100
    maximum = 1
    for i in range(start, limit):
        for j in range(start, limit):
            sum_ = sum(map(lambda x:int(x), str(i**j)))
            if sum_ > maximum:
                maximum = sum_
    return maximum

print "Answer by traditional method:", traditional()
