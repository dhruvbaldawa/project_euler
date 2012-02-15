"""
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the
following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations
def traditional():
    # Initialization
    start = 0
    limit = 9

    # Get the permutations of digits
    p_list = [x for x in permutations(range(start, limit+1))]
    divisors = [2,3,5,7,11,13,17]
    l=[]
    
    for permutation in p_list:
        # Discard the permutations starting with 0
        if permutation[0] == 0:
            continue
        # Convert numbers to strings and then list of strings
        # to a single string
        str_temp = [str(x) for x in permutation]
        str_temp = reduce(lambda x, y: x+y, str_temp)

        # Check for the divisibility
        breaked = False
        for i in range(1, len(str_temp)-2):
            temp = int(str_temp[i:i+3]) % divisors[i-1]
                
            if temp != 0:
                breaked = True
                break

        if breaked == False:
            l.append(int(str_temp))

    return sum(l)

print "Answer:", traditional()
