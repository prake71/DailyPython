'''
37. Personal Info Formatter

Write a Python program that displays your name, age, and address on
three different lines.

from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php


'''


personal_info = {"name" : "Peter", "age" : 54, "address" : "Sommerstr. 11 / 36199 Rotenburg"}

print(personal_info["name"])
print(personal_info["age"])
print(personal_info["address"])

for k in list(personal_info.keys()):
    print("{key}: {info}".format(key = k.capitalize(), info = personal_info[k]))

