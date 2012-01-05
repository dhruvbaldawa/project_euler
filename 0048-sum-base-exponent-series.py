"""
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
def power(base, exponent):
    if exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

def traditional():
    limit = 1000
    sum_ = 0
    for i in range(1, limit + 1):
        base = i
        exponent = i
        # Magic one-liner !!
        ans = base ** exponent
        sum_ = sum_ + ans
    return str(sum_)[-10:]

print "Answer by traditional method:", traditional()
