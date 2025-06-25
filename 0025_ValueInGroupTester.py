'''
2025-05-06 17:48:57 +0200

Write a Python program that checks whether a specified value is
contained within a group of values.

Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''


def is_in_group(elem: int, group: list):
    for i in range(len(group)):
        if elem == group[i]:
            return True
    return False


def is_in_group2(elem: int, group: list):
    return elem in group


print(is_in_group(3, [1, 5, 8, 3]))
print(is_in_group(-1, [1, 5, 8, 3]))
print(is_in_group2(3, [1, 5, 8, 3]))
print(is_in_group2(-1, [1, 5, 8, 3]))
