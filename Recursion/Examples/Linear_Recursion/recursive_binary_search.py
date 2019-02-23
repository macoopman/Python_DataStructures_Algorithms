"""
Recursive Binary Search:
locate a target value within a "sorted" sequence of n elements
Three Cases:
    - target == data[mid] - found
    - target < data[mid] - recur the first half of the sequence
    - target > data[mid] - recur the last half of the sequence

Runtime => O(log n)
"""

def binary_search(data, target, low, high):
    """ Return True if target is found in indicated portion of a Python List """

    if low > high:                  # Base Case: interval is empty; no match
        return False
    else:
        mid = (low + high) // 2             # find new mid point
        if target == data[mid]:             # found your target - exit search
            return True
        elif target < data[mid]:
            # recur on the ortion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recure on the portion right of the middle
            return binary_search(data, target, mid+1, high)
