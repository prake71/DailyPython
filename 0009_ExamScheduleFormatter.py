'''
Write a Python program to display the examination schedule. (extract
the date from exam_st_date).

exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

# import re
#exam_date = ""
# pattern = re.compile(r"\d+,\s\d+,\s\d+,\s")
exam_date = input("DD, MM, YYYY: ")
    
exam_st_date = exam_date.split(",")
print(exam_st_date[0] + " / " + exam_st_date[1] + " / " + exam_st_date[2])
