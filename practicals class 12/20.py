'''Define a function lowerAlpha(st) in Python that creates and returns a list
of all lowercase alphabets present in a string passed as argument to it.
e.g. if the string is, st= "Hello NCS"
then the function should return: [ 'e', 'l', 'l', 'o' ]'''
def lowerAlpha(st):
    alphabets = [c for c in st if c.islower()]
    print(alphabets)

st = str(input('Enter a string: '))
lowerAlpha(st)