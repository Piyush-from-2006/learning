'''Define a function ZeroEnding(SCORES) to add all those values in the list
of SCORES, which are ending with zero (0) and display the sum.
e.g. If the list SCORES contain [200, 456, 300, 100, 234, 678]
The sum should display the sum as: 600'''

def ZeroEnding(SCORES):
    sum = 0
    for i in SCORES:
        if i%10==0:
            sum+=i
        else:
            continue
    print(sum)
a=eval(input('enter score'))
ZeroEnding(a)
