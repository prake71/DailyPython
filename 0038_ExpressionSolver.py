'''
https://www.w3resource.com/python-exercises/python-basic-exercises.php

38. Expression Solver

Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49


'''

def expr(x,y):
    result = (x+y) * (x+y)
    result = "({} + {}) ^ 2 = {}".format(x,y,result)
    return result

x = 4
y = 3

print(expr(4,3))

