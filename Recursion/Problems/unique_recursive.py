# unique_recursive.py

"""
Perform a recursive search through a sequence to determine if the sequence
contains all unique characters
- domain is all valid ascii letters and numbers 0-9
- case insensitive
"""


def uniq(L):
    def uniq_recursive(L, char_set):
        # base case
        if len(L) == 1:                         # if len is 1 then we are at the final element
            if L[0] not in char_set:            # if final element is unique then entire sequence is unique
                return True
            else:
                return False

        if L[0] not in char_set:                # if current char is not in set then it is also unique
            char_set.add(L[0])                  # add to set
        else:
            return False
        return uniq_recursive(L[1:], char_set)   # recurs through list, removing one element per step


    valid = 'abcdefghijklmnopqrstuvwxyz1234567890'
    L = L.lower()
    # create new list: must be a valid char from above, no spaces
    valid_list = [character for character in L if character in valid]
    char_set = set()
    return uniq_recursive(valid_list, char_set)



if __name__ == "__main__":
    user_str = input("Enter string > ")
    print(uniq(user_str))
