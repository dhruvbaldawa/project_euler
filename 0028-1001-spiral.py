"""
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
def the_brute_force_thought():
    grid_size = 1001
    assert grid_size % 2 == 1
    sum = 1

    for i in range(2, grid_size + 1):
        if i % 2 == 0:
            # Generates 5, 17, 37...
            x = i ** 2 + 1
            # Generates 3, 13, 31...
            y = x - i
            sum = sum + x
            sum = sum + y
            print i, ":", x, ":", y
        else:
            # Generates 9, 25, 49...
            x = i ** 2
            # Generates 7, 21, 43...
            y = x - i + 1
            sum = sum + x
            sum = sum + y
            print i, ":", x, ":", y

    return sum
print "Answer:", the_brute_force_thought()
