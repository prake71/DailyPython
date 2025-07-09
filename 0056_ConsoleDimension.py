'''

from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

56. Console Dimensions

Write a Python program to get the height and width of the console window.

'''

import os

# this is not working inside emacs
try:
    size = os.get_terminal_size()
    print(size)
    print(f"Columns: {size.columns}, Rows: {size.lines}")
except OSError:
    print("unable to get terminal size.")
    

