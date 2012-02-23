"""
Problem 32

We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
from collections import Counter
def brute_force():
    # Initialization
    start = 1
    end = 9999
    l = []
    
    for i in range(start, end):
        j = i
        c = Counter() # Counter for each number
        flag = True # To check if the number can be considered or not
        answer = "" # The concatenated product
        while j <= 9999:
            c.clear()
            product = i * j
            answer = str(i)+str(j)+str(product)
            
            c.update(answer)
            # Break if there are 9 digits
            if sum(c.values()) > 9:
                break
                
            # Checking if all the numbers are present and there are exactly 9
            # print c, i, j
            if len(c) == 9 and sum(c.values()) == 9:
                l.append((i, j, answer, str(product)))
            j += 1
    
    # Finding the sum of products and neglecting the numbers with 0
    ans = sum(set([int(x[3]) for x in l if '0' not in x[2]]))
    return ans
    
print "Answer:", brute_force()
