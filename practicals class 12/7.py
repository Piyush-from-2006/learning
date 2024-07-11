'''Define a function in python that displays n-terms of a fibonacci series. The
function should accept n as parameter.'''
n = int(input("Enter a number: "))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(n)