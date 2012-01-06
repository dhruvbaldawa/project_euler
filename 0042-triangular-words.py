"""
Problem 42
The nth term of the sequence of triangle numbers is given by, tn = n(n+1) / 2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import math
def triangle_numbers(limit = 100):
    """
    Generates triangular numbers and finds number of its divisors
    """
    ans = []
    for n in range(1, limit + 1):
        # nth triangular number is given by the formula below
        n_triangle = n * (n + 1) / 2
        ans.append(n_triangle)
    
    return ans

def the_obvious_way():
    f = open("words.txt")
    
    words = f.read()[1:-1] # eliminating the first and last "
    words = words.split('","') # a workaround to skip the csv parsing
    
    count = 0
    
    # the preceding space is because we want alphabets with indices 1..26
    letters = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # find the longest word and find its length
    max_length = len(reduce(lambda x,y: max(x, y, key=len), words))
    max_number_per_alphabet = 26
    
    tri_numbers = triangle_numbers(26 * max_length)
    
    for word in words:
        total = sum([letters.index(x) for x in word])
        if total in tri_numbers:
            count = count + 1
        
    return count
        
print "Answer by the obvious way:", the_obvious_way()
