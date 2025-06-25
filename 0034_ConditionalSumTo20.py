'''
2025-05-22 11:53:15 +0200

Conditional Sum to 20

Write a Python program to sum two given integers. However, if the sum
is between 15 and 20 it will return 20.


'''


def mysum(a: int, b: int):
    c = a + b
    if (c in range(15, 20)):
        return 20
    else:
        return c


a = int(input("num a: "))
b = int(input("num b: "))

print(mysum(a, b))

print(mysum(14, 1))
assert mysum(14, 1) == 20
assert mysum(19, 1) == 20
assert mysum(18, 3) == 21
assert mysum(17, 3) == 20
assert mysum(10, 9) == 20
assert mysum(1, 1) == 2

