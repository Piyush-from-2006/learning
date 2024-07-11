'''Write a script in Python to perform all arithmetic operations
(**, *, /, //, %, +, -) between two numbers. The program should
accept the two operands and the operator, performs the operation
and displays the desired result. '''
j=int(input("enter 1st number: "))
k=int(input("enter 2nd number: "))
e=j**k
a=j+k
d=j/k
dd=j//k
s=j-k
m=j*k
r=j%k
print("exponent", e)
print("multiplication",m)
print("division",d)
print("floor division",dd)
print("modulus/remainder",r)
print("addition",a)
print("subtraction", s)
