"""
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
Find the largest palindrome made from the product of two 3-digit numbers
"""
def traditional():
    """
    Nothing fancy in this function, just checks for palindromes
    """
    palindromes = []
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            product = i * j
            product_str = str(product)
            if product_str == product_str[::-1]:
                palindromes.append(product)
    return max(palindromes)

def a_little_step_up():
    """
    Tiny optimizations over the previous approach
    """
    palindromes = []
    for i in range(999, 100, -1):
        if i % 11 == 0:
            # If i is divisible by 11, check for all j's
            x = range(i, 100, -1)
        else:
            # If i is not divisible by 11, check for all j's divisible by 11
            x = range(i - (i % 11), 100, -11)
            
        for j in x:
            product = i * j
            product_str = str(product)
            if product_str == product_str[::-1]:
                palindromes.append(product)
    return max(palindromes)

    
print "Answer by traditional method: ", traditional()
print "Answer by optimized method: ", a_little_step_up()
