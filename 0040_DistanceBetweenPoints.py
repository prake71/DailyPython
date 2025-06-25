'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

40. Distance Between Points

Write a Python program to calculate the distance between the points
(x1, y1) and (x2, y2)

'''
from math import sqrt

point_a = str(input("Point a (x, y): ")).split(",")
point_b = str(input("Point b (x, y): ")).split(",")

print(point_a, point_b)

dx = float(point_a[0]) - float(point_b[0])
dy = float(point_a[1]) - float(point_b[1])

d = sqrt(dx**2 + dy**2)

print(d)
