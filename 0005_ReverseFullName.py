'''
Write a Python program that accepts the user's first and last name and
prints them in reverse order with a space between them.
'''
last = input("Your lastname: ")
first = input("Your firstname: ")

name = first + " " + last

name_len = len(name)
name = name.lower()

for i in range(len(name)-1,-1,-1):
    print(name[i],end='')
print()


    
