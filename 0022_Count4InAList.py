'''
Write a Python program to count the number 4 in a given list.
'''
count4 = 0

mylist = [1,2,3,4,5,6,7,3,4,5,3,5,3,4,4] # 4 times 4

for i in mylist:
    if i == 4:
        count4 += 1

print("There are {n} times 4 in the list!".format(n = count4))

# variant b

count4 = mylist.count(4)
print("There are {n} times 4 in the list!".format(n = count4))
