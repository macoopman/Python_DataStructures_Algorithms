"""
Using two recusions (one for the first half, one for the last), we can sum up
the halfs and then add them together
"""

def binary_sum(S, start, stop):
    if start >= stop:                       # zero element in slice
        return 0
    elif start == stop-1:                   # one element in slice
        return S[start]
    else:                                   # 2 or more elments in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
