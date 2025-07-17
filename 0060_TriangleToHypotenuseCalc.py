'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

60. Triangle Hypotenuse Calculator

Write a Python program to calculate the hypotenuse of a right angled triangle. 
'''
from math import sqrt

# Pythagoras
# a² + b² = c² --> c = sqrt(a² + b²)

a = float(input("length of base: "))
b = float(input("length of atitude: "))

c = sqrt(a**2 + b**2)

print("length of hypotenuse: ", c)

