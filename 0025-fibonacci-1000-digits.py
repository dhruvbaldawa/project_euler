"""
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
def fibonacci():
    """
    Just the usual fibonacci generator which starts from 1,2,3,..
    """
    a = 1
    b = 1
        
    while True:
        yield a
        sum_ = a + b
        a = b
        b = sum_
        
def traditional():
    """
    Function to calculate sum of the usual fibonacci
    """
    length = 1000
    counter = 0
    for x in fibonacci():
        counter = counter + 1
        if len(str(x)) >= length:
            break
    return counter


print "Answer by traditional method:",traditional()
