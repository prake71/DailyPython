'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

49. Directory Files Lister

Write a Python program to list all files in a directory. 
'''

import os

path = "."

# option 1
for filename in os.listdir(path):
    print(filename)

# option 2
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
