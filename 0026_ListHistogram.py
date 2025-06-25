'''
2025-05-07 15:43:40 +0200

Write a Python program to create a histogram from a given list of integers.
'''


mylist = [6, 8, 8, 3, 3, 9, 2, 3, 4, 6, 2, 9, 0, 5, 7, 8, 3, 3, 6, 5,
          3, 2, 2, 3, 3, 8, 9, 5, 3, 8, 8, 9, 1, 0, 0, 7, 5, 3, 3, 1,
          0, 3, 5, 0, 4, 1, 8, 6, 5, 4]


print(mylist.count(5))
mylist.sort()
print(mylist)

print(mylist[-1])

for i in range(mylist[0], mylist[-1]+1, 1):
    print(str(i) + ": " + "*" * mylist.count(i))
