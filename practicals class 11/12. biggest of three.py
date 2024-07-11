#Write a script in Python to find the biggest of three numbers.
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))
if num1 >= num2:
    if num1 >= num3:
        biggest = num1
    else:
        biggest = num3
elif num2 >= num3:
    biggest = num2
else:
    biggest = num3
print("The biggest number is:", biggest)