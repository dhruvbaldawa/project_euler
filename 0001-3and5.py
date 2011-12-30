"""
Problem 1
Add all the natural numbers below one thousand that are multiples of 3 or 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def bruteforce():
    sum_ = 0
    number = 1000
    
    # Iterate over all the numbers and add those satisfy the condition
    for x in range(1, number):
        if x % 3 == 0 or x % 5 == 0:
            sum_ = sum_ + x
    print sum_

def divisibility():
    sum_ = 0
    number = 1000
    
    # Find the numbers divisible by 3
    l = range(1, number)
    number_three = len(l) / 3
    # This is basically sum(1..n) = n*(n+1)/2
    sum_three = number_three * (number_three + 1)/2
    
    # Find the numbers divisible by 5
    number_five = len(l) / 5
    # This is basically sum(1..n) = n*(n+1)/2
    sum_five = number_five * (number_five + 1)/2
    
    # Find the number of numbers divisible by 15
    number_fifteen = len(l) / 15
    # This is basically sum(1..n) = n*(n+1)/2
    sum_fifteen = number_fifteen * (number_fifteen + 1)/2
    
    sum_ = 3 * sum_three + 5 * sum_five - 15 * sum_fifteen
    print sum_

bruteforce()
divisibility()
