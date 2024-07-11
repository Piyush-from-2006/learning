'''Write a script in Python to read the contents of a file "ABC.TXT" and
count the number of occurrences of the alphabet 'a' in it.'''
file=open('abc.txt','r')
text = []
count=0
for char in file.read():
    if(char.lower()=='a'): count+=1
print("Number of times 'a' is found:",count)
file.close()