"""
Raise a number x to and arbitrary nonnegative integer, n
"""

"""
Trival Solution:  x^n = x * x^n-1 for n > 0
Runtime -> O(n)
"""

def power(x, n):
    """ Compute the value x**n for integer n"""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
