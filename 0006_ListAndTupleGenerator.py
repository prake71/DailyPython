'''
Write a Python program that accepts a sequence of comma-separated
numbers from the user and generates a list and a tuple of those
numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

sample_list = []
sample = None

while sample != "":
    sample = input("Type in your sample data (Return for exit)")
    if sample.isnumeric():
        sample_list.append(sample)

print(sample_list)
print(tuple(sample_list))


