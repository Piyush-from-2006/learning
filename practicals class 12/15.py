 
'''Define a function updateList(L) in Python that updates the contents of a
list in such a way that all the odd numbers present in the list should be
multiplied by 2 and all the even numbers should be divided by 2.'''
def updateList(L):
    for i in range(len(L)):
        if L[i] % 2 == 0:
            L[i] = L[i] // 2
        else:
            L[i] = L[i] * 2
    print(L)
L=eval(input('input list'))
updateList(L)
