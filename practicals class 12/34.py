'''Write a script in Python to count the total number of occurrences of the
word 'the' in a file "NOVEL.TXT".'''
filename = "NOVEL.TXT"
word_to_count = "the"
with open(filename, 'r') as file:
    content = file.read()
    count = 0
    index = content.find(word_to_count)
    while index != -1:
        count += 1
        index = content.find(word_to_count, index + 1)
    print("Total occurrences of 'the' in 'NOVEL.TXT':", count)
