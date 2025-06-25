# https://www.w3resource.com/python-exercises/python-basic-exercises.php

from datetime import date, timedelta

'''
Days Between Dates

Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

date1 = input("Insert start date: (yyyy, mm, dd) ")
date2 = input("Insert end date: (yyyy, mm, dd) ")

start = date1.replace(" ", "").split(",")
end = date2.replace(" ", "").split(",")


d0 = date(int(start[0]), int(start[1]), int(start[2]))
d1 = date(int(end[0]), int(end[1]), int(end[2]))

print(d0, d1)
print(d1 - d0)
