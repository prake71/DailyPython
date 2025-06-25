'''
from https://www.w3resource.com/python-exercises/python-basic-exercises.php

41. File Existence Checker

Write a Python program to check whether a file exists.


'''


from pathlib import Path

path = Path("./0041_FileExistenceChecker.py")
if path.is_file():
    print("File exists!")
else:
    print("File doesn't exist!")

