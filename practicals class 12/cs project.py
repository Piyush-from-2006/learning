import mysql.connector as mysql
dat=mysql.connect(host='localhost',user='root',password='shut up',database='db1')
cur=dat.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        department VARCHAR(255) NOT NULL,
        post VARCHAR(255) NOT NULL,
        salary VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        phone_no VARCHAR(15) NOT NULL,
        working_status VARCHAR(9) NOT NULL
    )
""")
dat.commit()

#adding new empolyee
def add_new():
    st='INSERT INTO employee values'
    id= int(input('enter id:'))
    name=input('enter name:')
    dept=input('enter department:')
    post=input('enter post:')
    sal=input('enter salary:')
    address=input('enter address:')
    phone=input('enter phone number:')
    work_stat=input('enter working status:')
    values=(id,name,dept,post,sal,address,phone,work_stat)
    cur.execute(st+str(values))
    dat.commit()
    print("Employee added successfully.")

#fetching all employee
def get_employees():
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee)

# Function to update employee details
def update_employee():
    sl='''UPDATE employee SET name='%s', department='%s',
    post='%s',sal='%s' address='%s', phone_no='%s',
    working_status='%s' WHERE id=%s'''
    id=int(input('enter employee id:'))
    name=input('enter name:')
    dept=input('enter department:')
    post=input('enter post:')
    sal=input('enter salary:')
    address=input('enter address:')
    phone=input('enter phone number:')
    work_stat=input('enter working status:')
    values=(name,dept,post,sal,address,phone,work_stat,id)
    cur.execute(sl%values)
    dat.commit()
    print("Employee details updated successfully.")

#delete from employee
def delete():
    id=int(input('enter employee id:'))
    sl = "DELETE FROM employee WHERE id="+str(id)
    cur.execute(sl)
    dat.commit()
    print("Employee deleted successfully.")

#front end
while True:
    print('WELCOME TO EMPLOYEE DATABASE.')
    print('what action would you like to perform?')
    print('1.add employee')
    print('2.see all employee data')
    print('3.update employee data')
    print('4.delete employee data')
    print('5.exit')
    f=int(input('enter choice:'))
    if f==1:
        add_new()
    elif f==2:
        get_employees()
    elif f==3:
        update_employee()
    elif f==4:
        delete()
    elif f==5:
        print('Have a good time ahead!')
        break
    else:
        print('wrong input')
        
