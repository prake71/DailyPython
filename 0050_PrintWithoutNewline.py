'''
50. Print Without Newline

Write a Python program to print without a newline or space. 

'''

# Reference: https://docs.python.org/3/tutorial/inputoutput.html

mystring = "The quick brown fox\n jumps over the lazy dog!!!"

# option 1
for my in mystring.split():
    print(my, end='')

print("\noption 2")
# option 2
print(mystring.replace(" ", "").replace("\n", ""))

# option 3
print(''.join(mystring.split()))


