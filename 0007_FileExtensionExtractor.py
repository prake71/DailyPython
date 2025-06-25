# https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''
Write a Python program that accepts a filename from the user and
prints the extension of the file.

Sample filename : abc.java
Output : java
'''

filename = input("Filename: ")

#dot = filename.find(".")

print("Extension: ", filename.split(".")[-1])




