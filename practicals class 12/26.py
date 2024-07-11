'''Write a function, lenWords(STRING), that takes a string as an 
argument and returns a tuple containing length of each word of a 
string. 
For example, if the string is "Come let us have some 
fun", the tuple will have (4, 3, 2, 4, 4, 3)'''

def lenWords(string):
    return tuple(len(word) for word in string.split())
s=str(input('enter a statement: '))
print(lenWords(s))