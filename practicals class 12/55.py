'''
Write a script in Python to read each record of a csv file "docs.csv", and
display the name(s) of those doctors whose specialization is "cardiology".
Assume that the csv file consists of records of hundreds of doctors in
tabular format under the following heads:
[id, doctor_name, dept, specialization]
'''
import csv
with open('docs.csv', 'r') as f:
    for i in csv.reader(f):
        if i[3].strip().lower() == 'cardiology':
            print(i[1])
