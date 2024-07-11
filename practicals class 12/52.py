'''
Write a script in Python to update the name of a student in a pickled
binary file “STU.DAT” that consists of data of hundreds of students stored
as objects of class dict in {Rollno : Name} format
'''
import pickle
f1 = open("STU.DAT", "rb")
lst = []
try:
    while True:
        x = pickle.load(f1)
        lst.append(x)
except EOFError:
    pass
f1.close()
rno = int(input("Enter the roll number of student whose name is to be updated: "))
name = input("Enter their new name:")
presence = False
for dicts in lst:
    for rnos in dicts:
        if rnos == rno:
            presence = True
            dicts[rno] = name
if presence == False:
    print("No student has that roll number")
else:
    f2 = open("STU.DAT",'wb')
    for i in lst:
        pickle.dump(i,f2)
    f2.close()
    print("Successfully updated!")