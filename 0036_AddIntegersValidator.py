'''
2025-05-28 14:07:48 +0200

https://www.w3resource.com/python-exercises/python-basic-exercises.php

Add Integers Validator

Write a Python program to add two objects if both objects are
integers.

'''
# type() returns the type of an object but does not check inheritance
# isinstance() checks if an object is an instance of a class or a
# subclass
# isinstance() is generally preferred for type checking, especially in
# the context of class inheritance.



def add_int(a, b):
    if (isinstance(a, int) and isinstance(b, int)):
        return a+b
    else:
        return None

def add_int2(a, b):
    if (type(a) == int and type(b) == int):
        return a+b
    else:
        return None


# Test cases with arbitrary objects
print(add_int(5, 10)) # Normal integers
print(add_int("5", "10")) # Strings that look like integers
print(add_int([1, 2], [3, 4])) # Lists
print(add_int({"a": 1}, {"b": 2}))# Dictionaries
print(add_int(5.5, 4.5)) # Floats
# Booleans in Python are implemented as a subclass of integers.
# https://docs.python.org/3/c-api/bool.html
print(add_int(True, False))  # Booleans
print(add_int(None, 5)) # None and integer
print(add_int(object(), object())) # Generic objects
print(add_int(complex(2, 3), complex(1, -1))) # Complex numbers
print(add_int((1, 2), (3, 4)))
print ("")
print(add_int2(5, 10)) # Normal integers
print(add_int2("5", "10")) # Strings that look like integers
print(add_int2([1, 2], [3, 4])) # Lists
print(add_int2({"a": 1}, {"b": 2}))# Dictionaries
print(add_int2(5.5, 4.5)) # Floats
print(add_int2(True, False))  # Booleans
print(add_int2(None, 5)) # None and integer
print(add_int2(object(), object())) # Generic objects
print(add_int2(complex(2, 3), complex(1, -1))) # Complex numbers
print(add_int2((1, 2), (3, 4)))
