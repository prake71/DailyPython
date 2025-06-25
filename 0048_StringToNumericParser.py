'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

48. String to Numeric Parser

Write a Python program to parse a string to float or integer.

'''

import re

my_number = None
pattern = r'[-+]?\d*\.?\d+'

my_string = input("Your String (looking like a number): ")
match = re.search(pattern, my_string)
if match:
    conv_str = match.group()
    if "." in conv_str:
        print("converting to float")
        my_number = float(conv_str)
    else:
        print("converting to interger")
        my_number = int(conv_str)
    print(my_number)

else:
    print("nothing to convert")

    




    




