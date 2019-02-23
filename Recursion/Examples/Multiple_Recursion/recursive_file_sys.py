"""
Recursively move through a file system
    - file systems written in a recurive fashon - tree
        - root = folder
        - leaves = files / subdirectories

Example: goal is to calculate the cumultive disk space used

Algorithm DiskUsage(path):
    Input: A string designated a path to a file-system entry
    Output: The cumulative disk space used by that entry and any nested entries
    total = size(path)                                                          # immediate disk space used by the entry
    IF path represents a directory THEN
        FOR each child entry stored within directory path DO
            total = total + DiskUsage(child)
    return total

Python Modules Used:

    - os.path.getsize(path)
        Return the immediate disk usage (measured in bytes) for the file or
        directory that is identified by the string path

    - os.ath.isdir(path)
        Return True if entry designated by string path is a directory; False otherwise

    - os.listdir(path)
        Return a list of strings that are the names of all entries within a directory
        designed by string path.

    - os.path.join(path, filename)
        compose the path string and filename string using an appropriate operating
        system separatory b/t the two

"""

import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""

    total = os.path.getsize(path)                       # account for direct usage
    if os.path.isdir(path):                             # if this is a directory,
        for filename in os.listdir(path):               # then for each child:
            childpath = os.path.join(path, filename)    # compose full path to child
            total += disk_usage(childpath)              # add child's usage - then resurs

    print('{0:<7}'.format(total), path)                 # descriptive output (optional)
    return total



if __name__ == "__main__":

    inp = input("Enter Starting Path > ")
    disk_usage(inp)
