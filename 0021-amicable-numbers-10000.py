"""
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def get_divisors(i, n = 2):
    """
    Recursive get divisors of a number
    """
    # Terminating condition, return 1
    if n > i**0.5:
        return [1]
    
    # If divisor
    if i % n == 0:
        if n != i/n:
            return_ = [n] + [i/n] + get_divisors(i, n + 1)
        else:
            return_ = [n] + get_divisors(i, n + 1)

        return return_
    # If not divisor
    else:
        return get_divisors(i, n + 1)

def amicable_numbers():
    # Initializing
    start = 4
    limit = 10000
    done = {}
    amicable = []
    for i in range(start, limit):
        # If already i is not an amicable number
        if i not in done:
            # get divisors of i and add them
            divisors = get_divisors(i)
            sum_i = sum(divisors)
            
            # check if the sum is withing the limit and not same as i
            if sum_i < limit and sum_i != i:
                sum_d = sum(get_divisors(sum_i))
                
                # if amicable number
                if i == sum_d:
                    done[sum_i] = True
                    done[i] = True
                    amicable.extend([i, sum_i])
    
    return sum(amicable)

print "Answer by traditional method:", amicable_numbers()
