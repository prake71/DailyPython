'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

42. Shell Mode Detector

Write a Python program to determine if a Python shell is executing in
32bit or 64bit mode on OS.


'''

# sys.maxsize is the maximum value representable by a signed word

# Generally, the maximum value representable by an unsigned word will
# be sys.maxsize * 2 + 1, and the number of bits in a word will be
# math.log2(sys.maxsize * 2 + 2)

import sys
import math


print("You are working in a {} bit shell.".format(math.log2(sys.maxsize * 2 +
                                                     3)))


# Test this program also in 32 bit shell on Windows.
# execute C:\Windows\SysWOW64\cmd.exe and run this program




