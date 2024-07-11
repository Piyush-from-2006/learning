'''Define a function in Python that accepts a tuple of numbers (Tup) as
parameter and returns the sum of only those elements of it whose unit
place is 7.
e.g. if the tuple is: T=(12,7,127,17,78,770)
then it should return sum as: 151'''

def sum7(T):
    print (sum(i for i in T if i % 10 == 7))
a=eval(input('enter a tuple'))

sum7(a)