# This exercise is from:
# https://www.w3resource.com/python-exercises/python-basic-exercises.php
#
from math import pi

'''
Write a Python program that calculates the area of a circle based on
the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

# user input
r = float(input("please enter radius of circle: "))


# calculate area of circle
# formula is: a = r**2 * PI
area = r**2 * pi

# output
print (f"The area of the circle with radius = {r} is: {area}")
