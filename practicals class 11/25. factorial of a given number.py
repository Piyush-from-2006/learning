n = int(input("Enter a number: "))
fact,o=1,n

if n == 0:
    print("Factorial of 0 is 1")
else:
    while n > 0:
        fact *= n
        n -= 1

    print("Factorial of", o, "is", fact)
