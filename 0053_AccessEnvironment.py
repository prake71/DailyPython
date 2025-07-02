'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

53. Access Environment Variables

Write a Python program to access environment variables.

'''

import os

# retrieve a PATH variable
path = os.environ["PATH"]
print(path)

# retrieve proxy
proxy = os.environ["HTTP_PROXY"]
print(proxy)

# set environment variable
os.environ["API_KEY"] = "abcdefghij"
print(os.environ["API_KEY"])



