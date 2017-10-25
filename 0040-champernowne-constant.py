"""
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""


def bruteforce():
    a = "0"
    i = 0
    while True:
        i += 1
        s = str(i)
        if len(a) <= 10**6:
            a += s
        else:
            break

    def d(n):
        return int(a[n])

    print(d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000))


bruteforce()
