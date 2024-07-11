'''Write a script in Python to count the total number of occurrences of such
words that begin with alphabet 't' in the file "STORY.TXT".
e.g. 'The', 'to', 'Today', 'Topper', etc.'''
filename = "abc.TXT"
with open(filename, 'r') as file:
    c = file.read().lower().split()
    #c=content.split()
    count,words = 0, ''
    for char in c:
        if char[0]=='t':
            count+=1
            word=''
    print("Total words starting with 't' is", count)