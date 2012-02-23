"""
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
from collections import Counter
def traditional():
    # Initialization
    start = 1
    end = 10000
    l = []
    
    for i in range(start, end):
        j = 1
        c = Counter() # Counter for each number
        flag = True # To check if the number can be considered or not
        answer = "" # The concatenated product
        while flag:
            product = i * j
            c.update(str(product))
            answer += str(product)
            # Checking if there are more than 9 numbers or not
            if len(answer) > 9:
                flag = False
            
            # Break if there are 9 digits
            elif len(answer) == 9:
                break
            j += 1
        
        # There are more than 9 digits so lets continue to next number
        if not flag:
            continue
        
        # Checking if all the numbers are present and there are exactly 9
        if len(c) == 9 and sum(c.values()) == 9:
            l.append((i, j, answer))
    
    # Finding the maximum number and neglecting the numbers with 0
    ans = max([int(x[2]) for x in l if '0' not in x[2]]) 
    return ans
    
print "Answer:", traditional()
