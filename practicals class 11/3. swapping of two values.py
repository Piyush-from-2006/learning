#Write a script in Python to swap / exchange value of two variables.
a = str(input("enter first value"))
b = str(input("enter second value"))
print("Before swap a and b = ", (a, b))
a, b = b, a
print("After swaping a and b = ", (a, b))