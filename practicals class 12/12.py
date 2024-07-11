'''Write a script in Python by defining a function Count37(NUM) that counts
all those numbers between 1 and NUM, which are either divisible by 3 or
7.
e.g. if N=10, then count should be: 4 (i.e. 3,6,7,9 are numbers)'''

def Count37(NUM):
    count = 0
    for i in range(1, NUM+1):
        if i % 3 == 0 or i % 7 == 0:
            count += 1
        else:
            continue
    print (count)
a=int(input('enter a number'))
Count37(a)