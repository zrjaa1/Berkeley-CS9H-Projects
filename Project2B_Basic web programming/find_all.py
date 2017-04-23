# Function Name: find_all
# Function Description: In a string, find the position of all the substrings.

# Function Input:
# -a_str: the string's name
# -sub: sub string that we are searching for

# Function Output: 
#  -a list that record all the start indexs of the sub string.

import string

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

print list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]
