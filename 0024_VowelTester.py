'''
Write a Python program to test whether a passed letter is a vowel (A, E, I, O, U) or not.

2025-05-05 14:56:26 +0200
'''


def vowel_check(char):
    char = char.upper()
    vowels = ["A", "E", "I", "O", "U"]
    if char in vowels:
        return True
    else:
        return False

def vowel_check2(char):
    char = char.lower()
    vowels = 'aeiou'
    return char in vowels

while 1:
    char = input("Your character: ")
    char = char[:1]
    if vowel_check2(char):
        print(f"{char} is vowel!")
    else:
        print(f"{char} is no vowel :-(")
    
        
