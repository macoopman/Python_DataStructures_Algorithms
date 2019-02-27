# palindrom_recursive.py
import string


def clean_word(word):
    """
    Input: unprocessed string
    Output: string with all space and special characters removed in lower case
    """
     return ("".join([char for char in word if char in string.ascii_letters or char in string.digits])).lower()


def is_palindrome(word):
    isa_palindrome = True
    clean = clean_word(word)
    if len(clean) == 0: return False
    if len(clean) == 1: return True             # assumes that a string of one char is a palindrom

    def palin(word, start, end, check):
        if start == end: return True
        if end - start == 1 and word[start] == word[end]:
            return True
        if end - start == 1 and word[start] != word[end]:
            print(1)
            return False
        if word[start] == word[end]:
            check = True
        else:
            return False

        return palin(word, start+1, end -1, check)


    if isa_palindrome == True:
        return palin(clean, 0, len(clean) - 1, isa_palindrome)
    else:
        return False


if __name__ == "__main__":
    print(f'is palin => {is_palindrome("Egad, a base life defiles a bad age.")}')
