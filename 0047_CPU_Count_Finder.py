'''
47. CPU Count Finder

Write a Python program to find out the number of CPUs used. 
'''
# Python 3 Standard Library
# https://docs.python.org/3/library/index.html


import multiprocessing
import psutil

print("Number of CPUs: ", os.cpu_count()) # from standard library
print("Number of CPUs: ", multiprocessing.cpu_count())
print("Number of CPUs: ", psutil.cpu_count())

