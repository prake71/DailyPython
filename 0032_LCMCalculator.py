'''
https://www.w3resource.com/python-exercises/python-basic-exercises.php

2025-05-19 21:36:55 +0200

LCM Calculator
Write a Python program to find the least common multiple (LCM) of two
positive integers.

finde den kleinsten gemeinsamen Vielfachen
'''

# In arithmetic and number theory, the least common multiple, lowest
# common multiple, or smallest common multiple of two integers a and
# b, usually denoted by lcm(a, b),


def lcm(a : int, b : int):
    a1 = a = abs(a)
    b1 = b = abs(b)
    ab = a1 * b1
    if a == 0 or b == 0:
        return 0
    alist = []
    blist = []
    alist.append(a)
    blist.append(b)
    
    while a <= ab or b <= ab:
        a += a1
        b += b1
        alist.append(a)
        blist.append(b)
    print(alist)
    print(blist)
    # ermittle das erste item, dass in beiden Listen vorkommt
    return [x for x in alist if x in alist and x in blist][0]

a = int(input("Number 1: "))
b = int(input("Number 2: "))
print(lcm(a,b))


# Basic cases
assert lcm(2, 3) == 6
assert lcm(4, 5) == 20
assert lcm(6, 8) == 24

# One number is a multiple of the other
assert lcm(3, 9) == 9
assert lcm(5, 15) == 15

# Same numbers
assert lcm(7, 7) == 7

# One number is 1
assert lcm(1, 10) == 10
assert lcm(1, 1) == 1

# Large numbers
assert lcm(123, 456) == 18696

# Negative numbers (assuming lcm returns positive result)
assert lcm(-4, 6) == 12
assert lcm(-7, -3) == 21
# Zero case (assuming lcm with 0 returns 0)
assert lcm(0, 5) == 0
assert lcm(0, 0) == 0







     

