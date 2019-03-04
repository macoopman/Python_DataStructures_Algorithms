"""
Given a unordered sequence of integers rearrange the integers so that all
evens are before the odds - Recursively

"""



def rearrange(L):
    """
    Input: sequence of integers
    Output: seperated - even/odd
    """
    def rearrange_inside(L, start, end):
        # Base Case
        if start >= end:
            return L
        # if outer edges are odd,even then swap to even, odd
        elif L[start] % 2 != 0 and L[end] % 2 == 0:
            L[start], L[end] = L[end], L[start]
            # recus and step in on both sides
            return rearrange_inside(L, start+1, end-1)
        else:
            # if end is odd then step in by one
            if L[end] % 2 != 0:
                return rearrange_inside(L, start, end-1)
            # if start is even then step foward by one
            if L[start] % 2 == 0:
                return rearrange_inside(L, start+1, end)
    return rearrange_inside(L,  0, len(L) - 1)


if __name__ == "__main__":
    L = [1,2,3,4,5]
    print(rearrange(L))

    L = [1,2,3,4,5,6]
    print(rearrange(L))

    L = [10,2,3,4,5,6]
    print(rearrange(L))

    L = [11,2,3,4,5,5]
    print(rearrange(L))
