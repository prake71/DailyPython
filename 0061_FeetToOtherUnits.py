'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

61. Feet to Other Units

Write a Python program to convert the distance (in feet) to inches, yards, and miles.
'''


# Inches, feet, yards, and miles are units of length in the US
# customary and imperial systems of measurement. There are 12 inches
# in a foot, 3 feet in a yard, and 1,760 yards (or 5,280 feet) in a
# mile.

distance = float(input("Distance measured in feet: "))

yards = distance / 3
inches = distance * 12
miles = yards / 1760

print(f"{distance} feet are {inches} in or {yards} yds or {miles} mis")

