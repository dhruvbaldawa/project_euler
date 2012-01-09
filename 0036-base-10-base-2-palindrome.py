"""
Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def number_to_binary(n):
    """
    This method converts a given number to binary
    It returns a list with the bits
    """
    binary = []
    while n != 0:
        binary.insert(0, n%2)
        n = n/2
    return binary

def full_adder(a, b, carry = 0):
    """
    A full adder, which adds 2 binary lists and 
    returns the resulting binary list.
    The binary list holds bits of decimal numbers
    """
    if len(a) < len(b):
        difference = len(b) - len(a)
        a = [0]*difference + a[:]
    elif len(a) > len(b):
        difference = len(a) - len(b)
        b = [0]*difference + b[:]
    
    assert len(a) == len(b)
    answer = []
    for i in reversed(range(len(a))):
        sum_ = (a[i] ^ b[i]) ^ carry
        carry = (a[i] & b[i]) | ((a[i] ^ b[i]) & carry)
        answer.insert(0, sum_)
    if carry == 1:
        answer.insert(0, carry) 
    
    return answer

def the_usual_method():
    start = 1
    limit = 1000000
        
    l = []
    for i in range(start, limit):
        # convert the number to binary
        bin = number_to_binary(i)
        # copy the binary
        bin_rev = last[:]
        # reverse the binary
        bin_rev.reverse()
        # check for the palindrome
        if bin_rev == bin and str(i)[::-1] == str(i):
            l.append(i)
    
    return sum(l)

print "Answer:", the_usual_method()
