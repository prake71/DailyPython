'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

57. Method Execution Time

Write a Python program to get the execution time of a Python method.

'''

import time
import math

def myfunc():
    my_val = 0
    for i in range(100000000):
        my_val = math.sqrt(i)

st = time.time()
myfunc()
et = time.time()

td = et - st
print("Execution time:", td, "seconds")

