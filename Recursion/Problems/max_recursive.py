
# max_recursive.py
"""
Problem 4.1:
Writee a recuresive algorithm fro finding the maximum element in a
sequence, S, on n element

1) Check for empty test
2) Check for list containing only 1 element - thats the max
3) check for list containing only 2 elements - test for max b/t the two
4) recuresively call the function reducing by one each time;
    base case: when only 2 elements
    coming out of the base case tests each element in the return statement
"""

import random


def rMax(L):
    """
    Recursive max function
    Input: sequence of n integers
    Output: max integer
    """
    if len(L) == 0: return 0          # list is empty
    if len(L) == 1: return L[0]
    if len(L) == 2: return max(L[0], L[1])
    return max(L[0], rMax(L[1:]))



if __name__ == "__main__":

    print("Recursive Max")
    print("Create Sequence")
    size = int(input("Size of sequence > "))
    domain = int(input("Max range > "))
    testList = [random.randint(0,domain) for x in range(size)]
    print("Original -> ", testList)
    print("Sorted (for ease of reading) -> ", sorted(testList))
    print(rMax(testList))
