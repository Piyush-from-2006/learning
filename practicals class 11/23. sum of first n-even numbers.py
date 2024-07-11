n = int(input("Enter the value of n: "))
count = 1
i = 2
total = 0

while count <= n:
    total += i
    i += 2
    count += 1

print("Sum of first", n, "even numbers is:", total)
