"""
A,lgorithm takes a list of unique integers and a k value that is the difference value;
Goal is to find all pairs of numbers that are k difference

Algorithm
1) Read in list - assumtiion is that it is already unique
2) Insert list into a dictionary - O(n)
3) Create a results list to append tuple pairs
4) Loop through the original list - test if each value + k or value - k is in dictionary
        IF in dictionary append to list
5) return list of tuples
"""


def k_pairs(L, k):

    search_dict = {}
    results = []
    for value in L:                                                             # generate dictionary based off list O(N)
        search_dict[value] = True
    for value in L:                                                             # iterate through L and check if each value +- k is in the dictionary
        if (value + k) in search_dict:
            pair = (min(value, (value + k)),max(value, (value + k)))            # create a pair that is smaller,larger
            if pair not in results: results.append(pair)                        # check if pair already exists - could all remove the value from the dictionary
        if (value - k) in search_dict:                                          # that would also remove any duplicates
            pair = (min(value, (value - k)),max(value, (value - k)))
            if pair not in results: results.append(pair)

    return sorted(results)                                                      # sorted adds it, but makes it prettier




if __name__ == "__main__":


    test_valued = [1,7,5,9,2,12,3]
    r = k_pairs(test_valued, 2)
    print(r)
