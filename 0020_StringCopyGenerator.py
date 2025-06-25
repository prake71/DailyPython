'''
Write a Python program that returns a string that is n (non-negative
integer) copies of a given string.
'''

def str_ntimes(text, n):
    n=abs(n)
    ntext = ""
    for i in range (0,n):
        ntext += " " + text
    return ntext

mystr = "The quick brown fox jumps over the lazy dog!"

print(str_ntimes(mystr, 10))

mystr = "abc"
print(str_ntimes(mystr, 10))
