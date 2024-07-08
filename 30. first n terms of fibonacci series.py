n = int(input("Enter the value of n: "))

if n <= 0:
    print("Invalid input")
else:
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1
