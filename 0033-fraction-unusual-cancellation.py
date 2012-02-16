"""
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
from fractions import Fraction
def replace_left(num, den):
    """
    Inserting the same number to the left of denominator and numerator
    """
    f_list = []
    for i in range(1, 10):
        if i == num or i == den:
            continue

        if Fraction(10*i+num, 10*i+den) == Fraction(num, den):
            f_list.append(Fraction(num, den))
    return f_list

def replace_right(num, den):
    """
    Inserting the same number to the right of denominator and numerator
    """
    f_list = []
    for i in range(1, 10):
        if i == num or i == den:
            continue

        if Fraction(10*num+i, 10*den+i) == Fraction(num, den):
            f_list.append(Fraction(num, den))
    return f_list

def replace_alternate(num, den):
    """
    Inserting the same number to the alternate sides of denominator and numerator
    """
    f_list = []
    for i in range(1, 10):
        if i == num or i == den:
            continue

        if Fraction(10*num+i, 10*i+den) == Fraction(num, den):
            f_list.append(Fraction(num, den))

        elif Fraction(10*i+num, 10*den+i) == Fraction(num, den):
            f_list.append(Fraction(num, den))
    return f_list

def traditional():
    f_list = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i==j:
                continue
            else:
                f_list.extend(replace_left(i, j))
                f_list.extend(replace_right(i, j))
                f_list.extend(replace_alternate(i, j))

    # Finding the product
    prod = 1
    for i in range(len(f_list)):
            prod *= f_list[i]

    return prod

print "Answer:", traditional()
