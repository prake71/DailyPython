'''
2025-05-26 16:49:49 +0200
Equality or 5 Rule Checker

Write a Python program that returns true if the two given integer
values are equal or their sum or difference is 5.

'''

def equal_or_five(a, b):
    if a == b:
        return True
    if a + b == 5:
        return True
    if a - b == 5:
        return True
    if b - a == 5:
        return True
    return False


print(equal_or_five(10, 5))
print(equal_or_five(3, 5))
print(equal_or_five(10, 10))
print(equal_or_five(7, 2))
print(equal_or_five(5, 5))
print(equal_or_five(8, 5))
print(equal_or_five(1, 9))
print(equal_or_five(5, 3))
print(equal_or_five(6, 6))
print(equal_or_five(0, 5))
print(equal_or_five(4, 4))


print(equal_or_five(2, 3)) # Summe = 5
print(equal_or_five(10, 5)) # Differenz = 5
print(equal_or_five(5, 0)) # Summe = 5
print(equal_or_five(7, 2)) # Differenz = 5
print(equal_or_five(3, 2)) # Summe = 5
print(equal_or_five(6, 6)) # Gleichheit
print(equal_or_five(0, 5)) # Summe = 5
print(equal_or_five(8, 3)) # Differenz = 5
print(equal_or_five(4, 1)) # Summe = 5
print(equal_or_five(9, 4)) # Differenz = 5
