"""
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# from python source itertools module
def permutations(iterable, r=None):
    'permutations(range(3), 2) --> (0,1) (0,2) (1,0) (1,2) (2,0) (2,1)'
    # convert the iterable to a tuple
    pool = tuple(iterable)
    
    # initializations
    n = len(pool)
    r = n if r is None else r
    
    # calculating the number of permutations
    indices = range(n)
    cycles = range(n-r+1, n+1)[::-1]

    # yield the iterable as it is (the first permutation)!
    yield tuple(pool[i] for i in indices[:r])
    
    while n:
        # the list is initialized as [r-1, r-2, .. 1]
        for i in reversed(range(r)):
            # decrease the cycle of ith element by 1
            cycles[i] -= 1
            if cycles[i] == 0:
                # build the permutations per iteration
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                # swap the indices
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def the_usual_method():
    index = 1000000
    count = 0
    for x in permutations(range(10)):
        count = count + 1
        if count == index:
            return reduce(lambda p,q: str(p) + str(q), x)

print "Answer by usual method:", the_usual_method()
