'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

62. Time to Seconds Converter

Write a Python program to convert all units of time into seconds. 
'''

# units of time: millenium, century, decade, year, day, hour, minutes, seconds
# see also: https://en.wikipedia.org/wiki/Unit_of_time

# 1 minute = 60 secs 
# 1 hour = 60 mins x 60 secs = 3600
# 1 day = 24 hrs x 60 mins x 60 secs = 86400
# 1 week = 7 days x 24 hrs x 60 mins x 60 secs = 604800
# 1 month = 4 weeks x 7 days x 24 hrs x 60 mins x 60 secs = 1:  2419200
# 1 year = 12 months x 4 weeks x 7 days x 24 hrs x 60 mins x 60 secs
# 1 decade = 10 years x 12 months x 4 weeks x 7 days x 24 hrs x 60 mins x 60 secs
# 1 century = 10 decades x 10 years x 12 months x 4 weeks x 7 days x
#             24 hrs x 60 mins x 60 secs
# 1 millenium = 10 centuries x 10 decades x 12 months x 4 weeks x 7
#               days x 24 hrs x 60 mins x 60 secs


def min_to_secs(value, unit):
    return value * 60

def hour_to_secs(value):
    return value * 3600

def day_to_secs(value):
    return value * 24 * 3600

def week_to_secs(value):
    return value * 7 * 24 * 3600

def month_to_secs(value):
    return value * week_to_secs(4)

def year_to_secs(value):
    return value * month_to_secs(12)

def decade_to_secs(value):
    return value * year_to_secs(10)

def century_to_secs(value):
    return value * decade_to_secs(10)

def millenium_to_secs(value):
    return value * century_to_secs(10)

print(decade_to_secs(200))
print(millenium_to_secs(2))


  
