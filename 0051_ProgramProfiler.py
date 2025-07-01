'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

51. Program Profiler

Write a Python program to determine the profiling of Python programs.

Note: A profile is a set of statistics that describes how often and
for how long various parts of the program executed. These statistics
can be formatted into reports via the pstats module.

'''

# https://docs.python.org/3/library/profile.html

import cProfile

def sum(a, b):
    print(a,b)
    sum = 0 
    for i in range(b):
        sum += a
    return sum

cProfile.run('sum(5000, 4000)')



