"""
Dynamic Array:
Provide a means to gro the array A that stores the elements of a list;

Steps:
1) Allocate a new array B with larger capacity (2x capacity)
2) Set B[i] = A[i] for i = 0,...,n-1,
3) Set A = B, that is, we hencefourth use B as the array supporting the list
4) Insert the new element in the array


"""

import ctypes                                                                   # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self, verbose=False):
        """Create an empty array"""
        self._n = 0                                     # count of actual items
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array
        self._verbose = verbose

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:                    # k must be valid b/t 0-n
            raise IndexError('invalid index')
        else:
            return self._A[k]

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:               # not enought room
            self._resize( 2 * self._capacity )      # double the capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                           # non-public utility
        """Resize interanl array to capacity c"""
        if self._verbose: print(f"Resizing: Starting Capacity = {self._capacity} : New Capacity = {c}")
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        """Return new areay with capacity c"""
        return (c * ctypes.py_object)( )




if __name__ == "__main__":

    print("Creating New Dynamic Array")
    x = DynamicArray(verbose=True)

    print('Appending: 1, "mike", 100, "hundred-mile" ')
    x.append(1)
    x.append("mike")
    x.append(100)
    x.append("hundred-mile")


    print("[ ", end="")
    for i in x:
        print(i,end=", ")
    print(" ]")
