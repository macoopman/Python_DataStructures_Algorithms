# reverse_recurs.py

"""
Write a short recursive Python function that takes a character string s and
outputs it reverse

Example: pots$pans -> snap&stop

"""


def reverse_r(seq):
    if len(seq) < 2 : return seq                            # seq is empty or one value
    if type(seq) == type('a'):                              # covert strings to list
        seq = list(seq)

    def r(seq, begin, end):                                 # prams: sequence, start, end
        if begin == end: return seq                         # BASE CASE: odd case
        if (end - begin) == 1:                              # BASE CASE: even case
            seq[begin], seq[end] = seq[end], seq[begin]     # perform swaps
            return seq
        else:
            seq[begin], seq[end] = seq[end], seq[begin]

        return r(seq, begin+1, end-1)                       # recursive step

    return "".join(r(seq,0,len(seq) - 1))                   # call interal fuction and join list before returning




if __name__ == "__main__":

    u_input = input("Enter string to be reversed: ")
    print(f"{u_input} --> {reverse_r(u_input)}")
