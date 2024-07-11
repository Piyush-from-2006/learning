'''
Write a script in Python to read each record of a csv "stud.csv" and
display the details of all the female students from it. Assume that the csv
file stores the records of hundreds of students under the following heads:
[rollno, name, gender, class_sec, phone]
'''
import csv
i_f = "stud.csv"
with open(i_f, 'r') as f:
    r = csv.reader(f)
    for i in r:
        if i[2].strip().lower() == 'female':
            print('Roll Number:', i[0], 'Name:', i[1])
            print('Gender:', i[2], 'Class Section:', i[3])
            print('Phone:', i[4])
            print()
