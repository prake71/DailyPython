'''
Write a Python program to print the documents (syntax, description
etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''
myfunc = input("Sample function: ")

myfunc = myfunc.replace("()", "")

print(help(myfunc))

print(eval(myfunc).__doc__)


