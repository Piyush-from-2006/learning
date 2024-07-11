#Write a script in Python to print first n-perfect squares.
n=int(input('enter the value of n: '))
for i in range(1,n+1):
    print(i*i,end="")
    print()