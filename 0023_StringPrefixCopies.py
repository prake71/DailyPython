'''
String Prefix Copies
Write a Python program to get n (non-negative integer) copies of the
first 2 characters of a given string. Return n copies of the whole
string if the length is less than 2.
2025-05-02 16:42:07 +0200
'''

mystrings =  ["The quick brown fox jumps", "over the lazy dog", "!", "and",
          "says \"Hello\"", ""]

modstr = ""

n = 10

def copy_prefix(mystr, n):
    returnstr = ""
    str2 = mystr[:2]
    if len(mystr) >= 2:
        for i in range(n):
            returnstr = returnstr + mystr[:2]
    elif len(mystr) < 2 and not (mystr == ""):
        for i in range(n):
            returnstr += mystr
    return returnstr


for mystr in mystrings:
    print (mystr)
    if len(mystr) == 0:
        continue
    else:
        print(copy_prefix(mystr,n))
