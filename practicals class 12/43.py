'''
 Write a script in Python to display the count of total number of characters,
lines and words in a single read from a file "SAMPLE.TXT".
'''
f = open("abc.txt", "r")
data = f.read()
f.close()
lines, words = data.split("\n"),data.split()
chars = 0
for i in words: chars+=len(i)
print("Number of lines: ", len(lines))
print("Number of words: ", len(words))
print("Number of characters: ", chars)