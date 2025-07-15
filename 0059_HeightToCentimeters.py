'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

59. Height to Centimeters

Write a Python program to convert height (in feet and inches) to centimeters. 
'''

# 1 foot = 30.48 cm
# 1 inch =  2.54 cm
import re

CONST_FT = 30.48
CONST_IN =  2.54

# re
# [0-9\.]+'[0-9\.]"
pattern = r"^(\d+(?:\.\d+)?)'(\d+(?:\.\d+)?)\"$"

height = input("Give me the height in ft and in (example 1'4\"): " )
print(height)
match = re.match(pattern, height)
if match:
    print("valid!")
    foot = float(match.group(1))
    inch = float(match.group(2))
    cm = foot * CONST_FT + inch * CONST_IN
    print(f"{foot}'{inch}\" = {cm} cm")
else:
    print("Your input was probably wrong!")
    


