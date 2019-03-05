"""
Implement a recrsive function with the signature find(path, name) that reports
all entries of the file system rooted at the given path having the given file name

"""


import os, sys

def find(path, name):
    """
    find and return list of all matches in the given path
    """
    found = []                                              # list of found items

    def find_recursive(path, name, found):                  # recursive function to traverse tree and append found items
        path_abs = os.path.abspath(path)                        # get the absolute path name
        dir_items = os.listdir(path_abs)                        # list all times in the currrent directory

        for item in dir_items:                                  # iterate over the dir list
            full_path = os.path.join(path_abs, item)                # get the full path name  path + filename/directory
            if os.path.isdir(full_path):                            # if is a directory
                find_recursive(full_path, name, found)                  # make recursive call to function

            if os.path.isfile(full_path):                           # if a file
                if item == name:                                        # check for name equality
                    found.append(full_path)                             # if true: add to list

    find_recursive(path, name, found)                       # call recursive function  

    return found







if __name__ == "__main__":
    if len(sys.argv) >= 3:
        path, name = sys.argv[1:]
    else:
        print("Usage: python3 find.py path name")
        sys.exit(1)

    found_files = find(path, name)

    print("Found Files:")
    for item in found_files:
        print("...", item)
