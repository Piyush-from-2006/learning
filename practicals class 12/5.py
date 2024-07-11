'''Define a function in Python that accepts a number as parameter and
checks whether it's prime or not'''
n = int(input("Enter a number: "))
def prime_or_not(n):
    if n <= 1:
       print(n, "is not a prime number")
    else:
       for i in range(2, n):
           if n % i == 0:
              print(n, "is not a prime number")
              break
       else:
          print(n, "is a prime number")

prime_or_not(n)