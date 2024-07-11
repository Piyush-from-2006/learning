'''Define a function search(d, x) in Python that checks whether an element
with key x is present in the dictionary d or not.'''
def search(d, x):
    if x in d:
        print(True)
    else:
        print(False)
d=eval(input('enter a dictionary: '))
x=(input('enter any key with thier corresponding value: '))
search(d,x)
