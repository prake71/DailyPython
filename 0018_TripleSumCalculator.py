'''
Write a Python program to calculate the sum of three given numbers. If
the values are equal, return three times their sum.
'''
nums = []

def all_equal(lst):
    return lst[:-1] == lst[1:]

for i in range(0,3):
    num = input("Number: ")
    nums.append(int(num))
if not all_equal(nums):
    print(sum(nums))
else:
    print(sum(nums)*3)
    
    

