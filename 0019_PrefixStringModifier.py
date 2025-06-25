'''
Write a Python program to get a newly-generated string from a given
string where "Is" has been added to the front. Return the string
unchanged if the given string already begins with "Is".
'''


def new_str(text):
    if text.find("Is", 0, 2) == -1:
        return "Is" + text
    else:
        return text


mystr = "Hello"
print(new_str(mystr))
mystr = "IsEmpty"
print(new_str(mystr))

