'''
Write a script in Python to create a pickled binary file “STU.DAT” to add
the data {Rollno : Name} of n-number of students into it
'''
import pickle
data = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    rollno = input("Enter Rollno for student"+ str(i + 1))
    name = input("Enter Name for student"+ str(i + 1))
    data[rollno] = name
with open("STU.DAT", 'wb') as file:
    pickle.dump(data, file)
print('Data saved')
