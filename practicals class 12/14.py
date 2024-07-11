'''Define a function revList(L) that should reverse the list elements. The
function accepts a list (L) as parameter and perform the updation(s) within
the same list (list being mutable).
e.g. if the list is: L=[10,15,61,35,22]
then list after executing the function, it should be: L=[22,35,61,15,10]
'''
def revList(L):
    n = len(L)
    for i in range(n//2):
        L[i], L[n-i-1] = L[n-i-1], L[i]
    print(L)
L = eval(input('enter a list'))
revList(L)
