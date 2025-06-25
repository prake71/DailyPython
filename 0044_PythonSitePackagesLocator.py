'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

44. Python Site Packages Locator

Write a Python program to locate Python site packages.

'''

# investigations

# site-packages is just the location where Python installs its modules.

# site-packages is the target directory of manually built Python
# packages. When you build and install Python packages from source
# (using distutils, probably by executing python setup.py install),
# you will find the installed modules in site-packages by default.



import sys
import site

print(sys.path[-1])

print(site.getsitepackages())




