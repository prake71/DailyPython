'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''
n = input("Give me your number: ")

strn = []
sum_strn = 0

# n + nn + nnn
for i in range(3):
    strn.append(str(n)*(i+1))

print(strn)
print(len(strn))
for k in range(len(strn)):
    print(strn[k])
    sum_strn += int(strn[k])
    
print("Sum: ", sum_strn)




    
