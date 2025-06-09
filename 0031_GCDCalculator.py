'''
https://www.w3resource.com/python-exercises/
2025-05-18

Write a Python program that computes the greatest common divisor (GCD)
of two positive integers.
'''


a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

# Der größte gemeinsame Teiler ist die ganze Zahl, durch die sowohl
# Zahl1 als auch Zahl2 dividiert werden können, ohne dass ein Rest
# bleibt.
gt = 0
m = 1
min_ab = min(a, b)
while m <= min_ab:
    if (a % m == 0) and (b % m == 0):
        gt = m
    m += 1
print(a,b,gt)



