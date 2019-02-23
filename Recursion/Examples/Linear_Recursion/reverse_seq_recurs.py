"""
Reverse the elements in a sequence using recursion;
Recursive Property:
    reversal of a sequence can be achieved by swapping the first
    and last elements and then recursively reversing the remaining elements
"""

def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start, stop]"""
    if start < stop - 1:                                    # if at least 2 elements
        S[start], S[stop-1] = S[stop-1], S[start]           # swap first and last
        reverse(S, start+1, stop-1)
        # walk from the outside in, swapping as you go. recursive call
        # until the middle 
