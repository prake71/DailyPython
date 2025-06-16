'''
from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

46. File Path and Name Finder

Write a Python program to retrieve the path and name of the file
currently being executed.

'''
import pathlib
import os

print('working directory: ', pathlib.Path.cwd())
print('current filename:  ', os.path.basename(__file__))



