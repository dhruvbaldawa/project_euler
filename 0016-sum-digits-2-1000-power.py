"""
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
def sum_of_digits(base, exponent):
    if exponent == 1:
        return base
    else:
        return base * sum_of_digits(base, exponent - 1)

def traditional():
    base = 2
    exponent = 1000
    # Magic one-liner !!
    ans = reduce(lambda x,y: int(x) + int(y), list(str(base ** exponent)))
    return ans

def recursive_method():
    # Splitting 2^n as 2*2^(n-1) = 2^(n-1) + 2^(n-1)
    base = 4
    exponent = 500
    sum_ = sum_of_digits(base, exponent)
    ans = reduce(lambda x,y: int(x) + int(y), list(str(sum_)))
    return ans

print "Answer by traditional method:", traditional()
print "Answer by recursive method:", recursive_method()
