'''
Write a Python program to test whether a number is within 100 of 1000
or 2000.
'''
myrange = 100

while 1:
    num = int(input("Your number: "))

    if (1000-myrange) <= num <= (myrange+1000):
        print("num is in range 1000 +/- 100")
    elif (2000-myrange) <= num <= (myrange+2000):
        print("num is in range 2000 +/- 100")
    else:
        print("number out of range!")


    
    
    
