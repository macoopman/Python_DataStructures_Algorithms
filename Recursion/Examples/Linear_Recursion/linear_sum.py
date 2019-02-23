"""
Linear Recursion: Each invocation of the body makes at most "one" new recursive call

"""

"""
Linear Sum:
    - compute the sum of a sequence, S, of n integers

Recursive Property:
    - The sum of all n integers in S is trivally 0, if n = 0m and otherwise
      that it is the sum of the first n-1integers in S plus the last element in S

"""

def linear_sum(S, n):
    """
    Input: A Sequence integers, total number to add 0 to n
    Output: return the sum of the first n numbers of sequence S
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
