'''Define a function in splitList(L) in python that accepts a list L as a
parameter and splits it into two parts, with one list consisting of all even
numbers & other list consisting of all odd numbers. The function should
return both the lists as well.'''

def splitList(L):
    even = []
    odd = []
    for i in L:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even,odd)
k=eval(input('enter a list of numbers'))
splitList(k)

