'''
Write a script in Python to create a csv file “stud.csv” and write the roll no,
name and marks of n-number of students into it.
'''
import csv
f = open('stud.csv','w',newline='')
wo = csv.writer(f)
n = int(input("Enter number of students:"))
for i in range(n):
    rno = int(input("Enter roll no:"))
    name = input("Enter name of student:")
    marks = input("Enter marks of student:")
    wo.writerow([rno,name,marks])
print("Successfully inserted data into stud.csv")
f.close()