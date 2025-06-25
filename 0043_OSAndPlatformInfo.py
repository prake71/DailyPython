'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

43. OS and Platform Info

Write a Python program to get OS name, platform and release information.
'''

import os
import platform
import sys

print("Operating System: ", platform.system())

print("OS Release: ", platform.release())
print("OS Release Info: ", platform.version())

#print(sys.platform)
