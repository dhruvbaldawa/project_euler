"""
Problem 14

The following iterative sequence is defined for the set of positive integers:

n ->  n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

cache = {}

def chain(n):
    """
    Memoized recursive function for the above expression
    """
    if n in cache:
        return cache[n]
    if n == 1:
        cache[1] = [1]
        return cache[1]
    else:
        if n % 2 == 0:
            cache[n] = [n] + chain(n / 2)
            return cache[n]
        else:
            cache[n] = [n] + chain(3 * n + 1)
            return cache[n]

def the_simple_chain():
    start = 2
    limit = 1000000
    max_length = 1
    max_num = 1
    for i in xrange(start, limit):
        chain = [i]
        last_element = i

        while last_element > 1:

            if last_element % 2 == 0:
                last_element = last_element / 2
            else:
                last_element = 3 * last_element + 1
            chain.append(last_element)

        # print i, ":", chain
        if len(chain) > max_length:
            max_num = i
            max_length = len(chain)

    return max_num

def the_recursive_chain():
    start = 2
    limit = 1000000
    max_length = 1
    max_num = 1

    for i in xrange(limit, start, -1):
        chain_list = [i]
        chain_list = chain(i)

        if len(chain_list) > max_length:
            max_length = len(chain_list)
            max_num = i
        # print i, ":", chain_list
        if i % 10000 == 0:
            print i, "done"

    return max_num

# print "Answer by simple chain method:", the_simple_chain()
print "Answer by recursive chain method:", the_recursive_chain()
