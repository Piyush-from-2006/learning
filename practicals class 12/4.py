'''Define a function in Python that accepts a number as parameter and
checks whether it's even or odd and prints the result'''
a=int(input("enter number: "))
def odd_or_not(a):
    if a%2==0:
        print("not odd")
    else:
        print("odd")
odd_or_not(a)