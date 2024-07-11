'''Write a script in Python to accept marks of a student in 5 subjects (Max marks-100)
and display the total, percentage and division as per the criteria:
>=60        -  1st Division
<60 & >=50  -  2nd Division
<50 & >=40  -  3rd Division
<40         -  Failed       '''
print('Please enter your marks out 100')
m1=float(input('enter marks of 1st subject: '))
m2=float(input('enter marks of 2nd subject: '))
m3=float(input('enter marks of 3rd subject: '))
m4=float(input('enter marks of 4th subject: '))
m5=float(input('enter marks of 5th subject: '))
total=m1+m2+m3+m4+m5
print('your total marks is: ', str(total))
p=total/5
print('percentage is: ', str(p))
if p<60:
    if p<50:
        if p<40:
            print('Failed')
        else:
            print('3rd Division')
    else:
        print('2nd Division')
else:
    print('1st Division')