"""
Calculate the factoral of a given number
"""
# factoral.py 

def factoral(n):
    if n == 0:
        return 1                            # if at base case return 1
    else:
        return n * factoral(n - 1)           # ie.e 5! -> 5 * 4!



if __name__ == '__main__':

    print(
    """

    Factoral Finder: Enter a positive integer
    """)

    while True:
        try:
            user_input = int(input('Enter # > '))
        except (ValueError, RecursionError) as e:
            print(e)
        else:
            if user_input < 1:
                print("Must be positive")
            else:
                break

    print(f"Factoral of {user_input} => {factoral(user_input)}")
