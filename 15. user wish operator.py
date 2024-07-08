'''Write a menu-driven script in Python to perform various arithmetic operations 
(**,*, /, //, %, +,-) between two numbers as per user choice.'''

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Division")
print("6. Modulo")
print("7. Power")

choice = input("Enter choice (1/2/3/4/5/6/7): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    result = num1 / num2
elif choice == '5':
    result = num1 // num2
elif choice == '6':
    result = num1 % num2
elif choice == '7':
    result = num1 ** num2
else:
    print("Invalid input")


print("Result:", result)
