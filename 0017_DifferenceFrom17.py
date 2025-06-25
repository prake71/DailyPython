'''
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
'''

while 1:
    numstr = input("Give me a number: ")
    if numstr.isnumeric():
        # difference
        num = int(numstr)
        diff17 = abs(num - 17)
        print("Difference to 17 is: ",diff17)
        print("Differencs x 2: ", diff17*2)
    else:
        break
