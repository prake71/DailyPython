'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php 

63. Absolute File Path Finder

Write a Python program to get an absolute file path.

'''

import os

# print current working directory
print(os.getcwd())

# print absolute file path including file name
# this is not working within Emacs when running in python-mode
# with C-c C-c
print(__file__)


