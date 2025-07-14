'''
from: https://www.w3resource.com/python-exercises/python-basic-exercises.php#google_vignette

58. Sum of First n Positives

Write a Python program to sum the first n positive integers.
'''


sum = 0 
n = int(input("How many number you want to sum up: "))

# Gauss'sche Summenformel
# sum(x) = n(n+1)/2
sum = n*(n+1)/2
print(sum)

# alternative with a loop
sum = 0
for i in range(n+1):
    sum += i

print(sum)

