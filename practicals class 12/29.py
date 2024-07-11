'''29. Write a script in Python to input the details of a student (Roll No, Full
Name, DOB, Gender and Class) and export it to a text file "STU.TXT".
Ensure that every time you execute the code and input the student
details, the details entered must be added to the same file.'''

count=int(input('how many students?'))
file=open('stu.txt','w')
for i in range (count):
    print('enter student', (i+1), 'below')
    rollno=(input('Roll number: '))
    fullname=input('Full name: ')
    DOB=input('date of birth: ')
    gender=input('Gender: ')
    Class=input('Class: ')
    rec=(rollno)+','+(fullname)+','+(DOB)+','+(gender)+','+(Class)+'\n'
    file.write(rec)
    print('student',(i+1),'details exported')
print('all records have been exported successfully')
file.close()