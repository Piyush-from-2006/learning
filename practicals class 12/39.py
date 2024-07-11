'''
Write a script in Python to read a text file "NOTES.TXT" line by line and
display each word separated by a "#".
filename = "NOTES.TXT"
'''
with open('abc.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        print(words[0]+'#')
