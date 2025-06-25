'''
2025-05-20 19:22:30 +0200

Triple Sum with Equality Rule

Write a Python program to sum three given integers. However, if two
values are equal, the sum will be zero.

'''

def sum(a, b, c):
    if a == b or a == c or b == c:
        return 0
    else:
        return a+b+c
   

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

sum(a,b,c)
