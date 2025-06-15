'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

45. External Command Runner

Write a Python program that calls an external command. 
'''

import subprocess

subprocess.run(["ls", "-l"])

# Another common way is os.system but you shouldn't use it because it
# is unsafe if any parts of the command come from outside your program
# or can contain spaces or other special characters, also
# subprocess.run is generally more flexible (you can get the stdout,
# stderr, the "real" status code, better error handling, etc.). Even
# the documentation for os.system recommends using subprocess instead.


