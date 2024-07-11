'''Define a function twoDigiCount(L) in python that accepts a list of numbers
(L) and returns the total number of two-digit numbers present in it.
e.g. if the list is: L=[10,2,125,61,200, 9, 22]
then, the function should return total two-digit numbers as : 3'''
def twoDigiCount(L):
    count = 0
    for num in L:
        if 10 <= num < 100:
            count += 1
    print (count)
l=eval(input('enter list of number'))

twoDigiCount(l)